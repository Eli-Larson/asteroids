import random 
import pygame 
from circleshape import CircleShape
from constants import * 


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,0),self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self, dt):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return 
        trajectory = random.uniform(20, 50)
        postive_rotate = self.velocity.rotate(trajectory)
        negative_rotate = self.velocity.rotate(-trajectory)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = postive_rotate * 1.2

        asteroid2=Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = negative_rotate * 1.2


class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
    def draw(self, screen):
        pygame.draw.circle(screen, (255,0,0), self.position, self.radius, width=2)
    def update(self, dt):
        self.position += self.velocity * dt