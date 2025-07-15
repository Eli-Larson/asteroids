import pygame
import random
import sys
from asteroidfield import AsteroidField 
from asteroid import *
from constants import *
from player import Player 

asteroid_group = pygame.sprite.Group()
updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
weapon_fire = pygame.sprite.Group()

Asteroid.containers = (asteroid_group, updatable, drawable)
Player.containers = (updatable, drawable)
AsteroidField.containers = (updatable,)
Shot.containers = (weapon_fire, updatable, drawable)



## MAIN FUNCTION TO RUN THE GAME.
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    clock = pygame.time.Clock()
    dt = 0 
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        for asteroid in asteroid_group:
            if player.collides_with(asteroid):
                print("Game Over!")
                sys.exit()
        for asteroid in asteroid_group:
            for bullet in weapon_fire:
                if bullet.collides_with(asteroid):
                    asteroid.split(dt)
                    bullet.kill()
        for entity in drawable:
            entity.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000


    




if __name__ == "__main__":
    main()