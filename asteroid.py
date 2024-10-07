import random
from circleshape import *
from pygame import *
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)
    
  def draw(self, screen):
    pygame.draw.circle(screen, "white", self.position, self.radius, 2)

  def update(self, dt):
    self.position += self.velocity * dt

  def split(self):
    self.kill()

    if self.radius <= ASTEROID_MIN_RADIUS:
      return
    
    angle = random.uniform(20, 50)
    smaller_radius = self.radius - ASTEROID_MIN_RADIUS

    asteroid_one_velocity = self.velocity.rotate(angle) * 1.2
    asteroid_two_velocity = self.velocity.rotate(-angle) * 1.2

    asteroid1 = Asteroid(self.position.x, self.position.y, smaller_radius).velocity = asteroid_one_velocity
    asteroid2 = Asteroid(self.position.x, self.position.y, smaller_radius).velocity = asteroid_two_velocity

