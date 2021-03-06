import pygame
from pygame import Vector2 as V
import os
from os import path
pygame.mixer.init()

# Global 

SCREEN_WIDTH        = 1600
SCREEN_HEIGHT       = 900
GRAVITY             = V(0, 0.1)
SCREEN_SIZE         = [SCREEN_WIDTH, SCREEN_HEIGHT]
SCREEN              = pygame.display.set_mode(SCREEN_SIZE) 
THEME_MUSIC         = ("sounds/music.wav")
WHITE               = (255, 255, 255)
BLACK               = (0, 0, 0)
FUEL_SOUND          = pygame.mixer.Sound("sounds/R2D2.wav")
FUEL_SOUND.set_volume(0.1)

# Player 

PLAYER_ACC          = 0.9
PLAYER_SPIN         = 4
PLAYER_MAX_THRUST   = 10
PLAYER_COLLISION    = 6

# Millennium falcon

MILLENNIUM_POS      = (300, 500)
MILLENIUM_CTRL      = [pygame.K_w, pygame.K_a, pygame.K_d, pygame.K_q]
MILLENIUM_H         = 90
MILLENIUM_W         = 80
MILLENIUM_SOUND     = pygame.mixer.Sound("sounds/millenium_sound.wav")
MILLENIUM_SOUND.set_volume(0.1)

# Star destroyer

STAR_POS            = (1400, 500)
STAR_CTRL           = [pygame.K_UP, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_PERIOD]
STAR_H              = 100
STAR_W              = 70
STAR_SOUND          = pygame.mixer.Sound("sounds/star_sound.wav")
STAR_SOUND.set_volume(0.04)

# Blaster

BLASTER_H           = 60
BLASTER_W           = 40
BLASTER_SPEED       = 4

# Explosion

img_dir = path.join(path.dirname(__file__), "animation")

EXPLOSION_ANIMATION = {}
EXPLOSION_ANIMATION["standard"] = []

for i in range(9):
    filename = "explosion0{}.png".format(i)
    image = pygame.image.load(path.join(img_dir, filename)).convert()
    image.set_colorkey(BLACK)
    img_standard = pygame.transform.scale(image, (200, 200))
    EXPLOSION_ANIMATION["standard"].append(img_standard)

IMAGE = EXPLOSION_ANIMATION["standard"][0]
EXPLOSION_SOUND     = pygame.mixer.Sound("sounds/explosion.wav")
EXPLOSION_SOUND.set_volume(0.1)
