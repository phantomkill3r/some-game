import pygame

class Grapple(pygame.sprite.Sprite):
    def __init__(self,x,y,player,grapplegp,leftb,rightb):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load('tile.png')
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.player=player
        self.grapplegp=grapplegp
        self.stick=False
        self.leftb=leftb
        self.rightb=rightb
        self.image.fill((0,255,0))

    def update(self):

        blockhitlist=pygame.sprite.spritecollide(self.player,self.grapplegp,False)
        for block in blockhitlist:
            if self.player.my>0:
                self.player.rect.bottom=block.rect.top
                self.player.my=0
            elif self.player.my<0:
                self.player.rect.top=block.rect.bottom
                self.player.my=0
                self.stick=True

        if self.stick==True:
            self.player.my=0
        if self.player.rect.left>self.rightb:
            self.stick=False
        elif self.player.rect.right<self.leftb:
            self.stick=False



