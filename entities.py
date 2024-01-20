import pygame
from settings import *
from spritesheet import *

class Entity(pygame.sprite.Sprite):
    def __init__(self, x, y, sprites, spriteW=0, spriteH=0):
        super().__init__()
        self.SpriteHeight = spriteH
        self.SpriteWidth = spriteW

        self.SpriteSheet = Spritesheet(filename=sprites)
        self.image = self.SpriteSheet.image_at((0,0, self.SpriteWidth, self.SpriteHeight))
        self.rect = self.image.get_rect(center=(x, y))
        self.Active = True
        self.AnimationTimer = 0
        self.CurrentSpriteIndex = 0
        self.Direction = "N"


    def ResizeSprite(self, ScaleFactor=2):
        self.image = pygame.transform.scale_by(self.image, ScaleFactor)
        self.rect = self.image.get_rect(center=(self.rect.centerx, self.rect.centery))
        
    
class Player(Entity):
    def __init__(self, x=0, y=0, sprites=None, spriteW=0, spriteH=0):
        Entity.__init__(self, x, y, sprites, spriteW=spriteW, spriteH=spriteH)
        self.image = pygame.transform.scale_by(self.image, 2)
        self.rect = self.image.get_rect(center=(self.rect.centerx, self.rect.centery))
        
    def WalkAnimation(self, speed=1):
        Directions = {
            "S": 0,
            "E": 1,
            "N": 2,
            "W": 3
        }
        AnimationTick = 200 * speed
        WalkSprites = 4
        
        CurrentTick = pygame.time.get_ticks()
        if CurrentTick - self.AnimationTimer >= AnimationTick:
            self.AnimationTimer = CurrentTick
            self.CurrentSpriteIndex = (self.CurrentSpriteIndex+1) % WalkSprites
            self.image = self.SpriteSheet.image_at((self.SpriteWidth*self.CurrentSpriteIndex,
                                                    self.SpriteHeight*Directions[self.Direction], 
                                                    self.SpriteWidth,
                                                    self.SpriteHeight))
            self.ResizeSprite()

            
        
        