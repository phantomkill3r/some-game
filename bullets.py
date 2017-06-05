import pygame

class Bullets(pygame.sprite.Sprite):
    def __init__(self,speed=10):
        pygame.sprite.Sprite.__init__(self)
        self.speed=speed
        self.image=pygame.Surface([10,5])
        self.rect=self.image.get_rect()
        self.image.fill((255,0,0))
        self.mx=self.speed
    def update(self):
        self.rect.x+=self.mx


