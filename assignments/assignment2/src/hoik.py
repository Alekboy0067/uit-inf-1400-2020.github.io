import pygame 
import math 
import parameter as P
from parent import Common

screen = pygame.display.set_mode([P.SCREEN_WIDTH, P.SCREEN_WIDTH])

# Class for hoik

class Hoik(Common):

    def __init__(self):

        super().__init__("pics/upvote.png", 80, 80)

    def update(self, flock, obstacles):
        
        edge = self.edge()
        separate = self.flock_separation(flock, P.HOIK_MAD)    
        avoid = self.object_avoid(obstacles)     

        self.speed = self.speed + (edge*2)                                      # Hoik, avoids edge
        self.speed = self.speed - (separate*3)                                  # Hoiks will seek out boids
        self.speed = self.speed.normalize() * P.MAX_SPEED_HOIK                  # Limit for speed
        self.speed = self.speed + (avoid*4)                                     # Avoid objects asteroids

        self.pos += self.speed

        self.dir = math.degrees(math.atan2(self.speed[1], self.speed[0]))       # Gets direction of image
        self.image = pygame.transform.rotate(self.rotation_image, -self.dir)    # Rotates image in the right direction                                   
        self.rect = self.image.get_rect(center=(self.rect.center))              # Get new rect
        self.rect.center = self.pos                                             # New center

        self.eat(flock)

        screen.blit(self.image, self.pos)                                       # Blit image to screen

    def eat(self, flock):

        pos = self.pos

        for boid in flock: 
            length = math.hypot(boid.pos[0] - pos[0], boid.pos[1] - pos[1])
            if length <= P.EAT_DIST:
                flock.remove(boid) 
