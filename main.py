import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from shot import Shot
from asteroidfield import AsteroidField
import sys

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")

        # player.update(dt)
        updatable.update(dt)
        # player.draw(screen)
        for obj in drawable:
            obj.draw(screen)

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.check_collision(shot):
                    #print("HIT")
                    asteroid.split()
                    shot.kill()
        
        for asteroid in asteroids:
            if asteroid.check_collision(player):
                print("GAME OVER!!!")
                #player.restart(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
                sys.exit(0)

        dt = game_clock.tick(60)/1000
        #print(dt)
        pygame.display.flip()

if __name__ == "__main__":
    main()