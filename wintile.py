import pygame

class WinTile(pygame.sprite.Sprite):
    def __init__(self,x,y,sx=20,sy=40):
        self.sizex=20
        self.sizey=40
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load('arrow.png').convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y