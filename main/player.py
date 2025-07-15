from circleshape import CircleShape
from constants import *
from asteroid import * 
import pygame


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0 
        self.player_timer = 0

 
# building the player object.
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    def draw(self, screen):
         surface = screen
         color = (255, 192, 203)
         points = self.triangle()
         width = 2 
         pygame.draw.polygon(surface, color, points, width)
        
## BUILDING THE SHOOT METHOD.

    def shoot(self, dt):
        if self.player_timer > 0:
            return 
        self.player_timer = PLAYER_SHOOT_COOLDOWN

        shot = Shot(self.position.x, self.position.y)
        bullet_velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        shot.velocity = bullet_velocity

      



## PLAYER MOVEMENT USING W,A,S,D
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt 
    
    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.player_timer -= dt

        if keys[pygame.K_a]:
            self.rotate(-dt)

        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_s]:
            self.move(-dt)

        if keys[pygame.K_w]:
            self.move(dt)

        if keys[pygame.K_SPACE]:
            self.shoot(dt)
        

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

