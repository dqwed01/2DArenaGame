import pygame
from pygame.locals import *
import sys
from settings import *
from entities import Player

class Game:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Arena Shooter") 
        
        self.players = pygame.sprite.GroupSingle()
        self.players.add(Player(x=SCREEN_WIDTH//2, y=SCREEN_HEIGHT//2,\
            sprites='assets/character.png', spriteW=16, spriteH=32))

    def display(self, *spriteGroups):
        background = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        background.fill("Black")
        self.screen.blit(background, (0,0))
        for spriteGroup in spriteGroups:
            spriteGroup.draw(self.screen)


    def run(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        for player in self.players:
            player.WalkAnimation()
        self.display(self.players) 
        pygame.display.update()
        