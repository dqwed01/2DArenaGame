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


    def ResizeSprite(self, ScaleFactor=2):
        self.image = pygame.transform.scale_by(self.image, ScaleFactor)
        self.rect = self.image.get_rect(center=(self.rect.centerx, self.rect.centery))
        

class MoveableEntity(Entity):
    def __init__(self, x=0, y=0, sprites=None, spriteW=0, spriteH=0):
        Entity.__init__(self, x, y, sprites, spriteW, spriteH)
        
        self.Active = True
        self.State = "Stand"
        self.AnimationTimer = 0
        self.CurrentSpriteIndex = 0
        self.Direction = "S"
    def WalkAnimation(self, WalkSprites, speed=1):
        Directions = {
            "S": 0,
            "E": 1,
            "N": 2,
            "W": 3
        }
        AnimationTick = 200 // speed
        
        CurrentTick = pygame.time.get_ticks()
        if CurrentTick - self.AnimationTimer >= AnimationTick and self.Active:
            self.AnimationTimer = CurrentTick
            self.CurrentSpriteIndex = (self.CurrentSpriteIndex+1) % WalkSprites
            self.image = self.SpriteSheet.image_at((self.SpriteWidth*self.CurrentSpriteIndex,
                                                    self.SpriteHeight*Directions[self.Direction], 
                                                    self.SpriteWidth,
                                                    self.SpriteHeight))
            self.ResizeSprite()
    
class Player(MoveableEntity):
    def __init__(self, x=0, y=0, sprites=None, spriteW=0, spriteH=0):
        MoveableEntity.__init__(self, x, y, sprites, spriteW=spriteW, spriteH=spriteH)
        self.image = pygame.transform.scale_by(self.image, 2)
        self.rect = self.image.get_rect(center=(self.rect.centerx, self.rect.centery))

    def Animate(self):
        keys=pygame.key.get_pressed()
        if keys[WALK_UP] or keys[WALK_DOWN] or keys[WALK_LEFT] or keys[WALK_RIGHT]:
            self.State = "Walk"
            if keys[WALK_UP]:
                self.Direction = "N"
            elif keys[WALK_DOWN]:
                self.Direction = "S"
            elif keys[WALK_LEFT]:
                self.Direction = "W"
            elif keys[WALK_RIGHT]:
                self.Direction = "E"
        else:
            self.State = "Stand"
        
        if self.State == "Walk":
            self.WalkAnimation(4)
        
                
        
        
            
        
        