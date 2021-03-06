import pygame 
import math 
import random 
import parameter as P
from pygame import Vector2 as V

screen = pygame.display.set_mode([P.SCREEN_WIDTH, P.SCREEN_WIDTH])

# Parent class for hoiks and boids

class Common():

    def __init__(self, pics, size_x, size_y):

        self.image = pygame.Surface([P.SCREEN_WIDTH, P.SCREEN_HEIGHT])      # Where the image is to be
        self.image = pygame.image.load(pics)                                # Loads boid image
        self.image = pygame.transform.scale(self.image, (size_x, size_y))   # Transform image to given scale
        self.rotation_image = self.image                                    # Used for rotating image 

        x = pygame.mouse.get_pos()[0]                                       # x posistion of mouse
        y = pygame.mouse.get_pos()[1]                                       # y posiition of mouse

        self.pos = x, y                                                     # Object position is mouse position

        self.rect = self.image.get_rect(center =(size_x/2, size_y/2))       # Center of image is its length and height divided by 2
            
        speed = (random.uniform(P.MIN_SPEED, P.MAX_SPEED),                  # Random (x, y) speed 
                random.uniform(P.MIN_SPEED, P.MAX_SPEED))
        self.speed = V(*speed)   
        self.dir = self.speed                                               # Direction is speed, used for rotating image later

    def edge(self):                                                         # Keeps objects within screen

        x = 0
        y = 0 

        if self.rect.centerx < 0 + P.WALL_DIST: 
            x = 1
        if self.rect.centerx > P.SCREEN_WIDTH - (1.5*P.WALL_DIST):
            x = -1
        if self.rect.centery < 0 + P.WALL_DIST:
            y = 1
        if self.rect.centery > P.SCREEN_HEIGHT - (1.5*P.WALL_DIST):
            y = -1

        new_dir = V(x, y)

        return new_dir
    
    def flock_separation(self, flock, dist):                                # Boids will try and avoid each other, also used
                                                                            # with hoiks for them to detect other boids
        separation = V(0, 0)
        pos = self.pos

        for boid in flock:
            if boid.pos != self.pos:
                length = math.hypot(boid.pos[0] - pos[0], boid.pos[1] - pos[1])  
                if length < dist:
                    separation -= (boid.pos - pos) * P.SEPARATION

        return separation

    def object_avoid(self, obstacles):                                      # Boids and hoiks alike will try and avoid obstacles

        avoid_obj = V(0, 0)
        posx = self.rect.centerx
        posy = self.rect.centery

        for asteroid in obstacles:
            length = math.hypot(asteroid.rect.centerx - posx, asteroid.rect.centery - posy)
            if length < P.ASTEROID_DIST:
                avoid_obj -= (asteroid.pos - self.pos) * P.ASTEROID_AVOID
                
        return avoid_obj