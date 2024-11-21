import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, width=2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        angle = random.uniform(20, 50)
        vel1 = self.velocity.rotate(angle)
        vel2 = self.velocity.rotate(-angle)
        r = self.radius - ASTEROID_MIN_RADIUS
        a1 = Asteroid(self.position[0], self.position[1], r)
        a1.velocity = vel1 * 1.2
        a2 = Asteroid(self.position[0], self.position[1], r)
        a2.velocity = vel2 * 1.2

