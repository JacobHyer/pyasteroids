import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys

def main():
  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

  clock = pygame.time.Clock()
  dt = 0

  # Groups
  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()
  shots = pygame.sprite.Group()

  # Add Sprites to Groups
  Player.containers = (updatable, drawable)
  Asteroid.containers = (updatable, drawable, asteroids)
  AsteroidField.containers = (updatable)
  Shot.containers = (updatable, drawable, shots)


  # Define Sprites
  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
  asteroid_field = AsteroidField()

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
      
    pygame.Surface.fill(screen,'black')
    for item in updatable:
      item.update(dt)
    for item in drawable:
      item.draw(screen)
    pygame.display.flip()
    for asteroid in asteroids:
      if asteroid.collisions(player):
        sys.exit("Game Over!")
      for shot in shots:
        if asteroid.collisions(shot):
          asteroid.split()
          shot.kill()
    dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
    