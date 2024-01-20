from win32api import GetSystemMetrics
import pygame

SCREEN_WIDTH = GetSystemMetrics(0) // 2
SCREEN_HEIGHT = GetSystemMetrics(1) // 2
WALK_UP = pygame.K_w
WALK_DOWN= pygame.K_s 
WALK_LEFT = pygame.K_a
WALK_RIGHT = pygame.K_d
WALK_KEYS = [WALK_UP, WALK_DOWN, WALK_LEFT, WALK_RIGHT]
