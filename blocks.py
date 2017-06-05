import pygame

class Block(pygame.sprite.Sprite):
    def __init__(self,x,y,mx=0,ret1=0,ret2=0,spikes=False,grapple=False,level1=False,level2=False,level3=False):
        pygame.sprite.Sprite.__init__(self)
        self.level1=level1
        self.level2=level2
        self.level3=level3
        self.spikes=spikes

        if self.level1==True:
            self.image=pygame.image.load('tile1.png').convert_alpha()
        if self.level2==True:
            self.image=pygame.image.load('tile2.png').convert_alpha()
        if self.level3==True:
            self.image=pygame.image.load('tile3.png').convert_alpha()
        if self.spikes==True:
            self.image=pygame.image.load('spikes.png').convert_alpha()

        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.mx=mx
        self.ret1=ret1
        self.ret2=ret2
        self.grapple=grapple
    def update(self):
        self.rect.x+=self.mx
        if self.rect.x>self.ret1:
            self.mx*=-1
        elif self.rect.x<self.ret2:
            self.mx*=-1
