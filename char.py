import pygame
from key import *

class CHAR(pygame.sprite.Sprite):
    def __init__(self,blockgp,x=0,y=0,mx=0,my=0,sx=30,sy=60,winy=400,winx=900,ai=False,ret1=0,ret2=0,ai1=False,ai2=False,player=False,aistay=None):
        pygame.sprite.Sprite.__init__(self)
        self.blockgp=blockgp
        self.mx=mx
        self.my=my
        self.sx=sx
        self.sy=sy
        self.winy=winy
        self.winx=winx
        self.ai=ai
        self.ai2=ai2
        self.ai1=ai1
        self.player=player
        self.aistay=aistay

        self.i1=pygame.image.load('i1.png').convert_alpha()
        self.i2=pygame.image.load('i2.png').convert_alpha()
        self.i3=pygame.image.load('i3.png').convert_alpha()
        self.i4=pygame.image.load('i4.png').convert_alpha()
        self.i5=pygame.image.load('i5.png').convert_alpha()
        self.i6=pygame.image.load('i6.png').convert_alpha()
        self.i7=pygame.image.load('i7.png').convert_alpha()
        self.i8=pygame.image.load('i8.png').convert_alpha()
        self.i9=pygame.image.load('i9.png').convert_alpha()
        self.i10=pygame.image.load('i10.png').convert_alpha()
        self.i11=pygame.image.load('i11.png').convert_alpha()
        self.i12=pygame.image.load('i12.png').convert_alpha()
        self.i13=pygame.image.load('i13.png').convert_alpha()
        self.i14=pygame.image.load('i14.png').convert_alpha()
        self.i15=pygame.image.load('i15.png').convert_alpha()
        self.i16=pygame.image.load('i16.png').convert_alpha()
        self.i17=pygame.image.load('i17.png').convert_alpha()
        self.i18=pygame.image.load('i18.png').convert_alpha()

        self.r1=pygame.image.load('r1.png').convert_alpha()
        self.r2=pygame.image.load('r2.png').convert_alpha()
        self.r3=pygame.image.load('r3.png').convert_alpha()
        self.r4=pygame.image.load('r4.png').convert_alpha()
        self.r5=pygame.image.load('r5.png').convert_alpha()
        self.r6=pygame.image.load('r6.png').convert_alpha()
        self.r7=pygame.image.load('r7.png').convert_alpha()
        self.r8=pygame.image.load('r8.png').convert_alpha()
        self.r9=pygame.image.load('r9.png').convert_alpha()
        self.r10=pygame.image.load('r10.png').convert_alpha()
        self.r11=pygame.image.load('r11.png').convert_alpha()
        self.r12=pygame.image.load('r12.png').convert_alpha()

        self.s1=pygame.image.load('s1.png').convert_alpha()
        self.s2=pygame.image.load('s2.png').convert_alpha()
        self.s3=pygame.image.load('s3.png').convert_alpha()
        self.s4=pygame.image.load('s4.png').convert_alpha()
        self.s5=pygame.image.load('s5.png').convert_alpha()
        self.s6=pygame.image.load('s6.png').convert_alpha()
        self.s7=pygame.image.load('s7.png').convert_alpha()
        self.s8=pygame.image.load('s8.png').convert_alpha()
        self.s9=pygame.image.load('s9.png').convert_alpha()
        self.s10=pygame.image.load('s10.png').convert_alpha()
        self.s11=pygame.image.load('s11.png').convert_alpha()
        self.s12=pygame.image.load('s12.png').convert_alpha()
        self.s13=pygame.image.load('s13.png').convert_alpha()
        self.s14=pygame.image.load('s14.png').convert_alpha()
        self.s15=pygame.image.load('s15.png').convert_alpha()
        self.s16=pygame.image.load('s16.png').convert_alpha()
        self.s17=pygame.image.load('s17.png').convert_alpha()
        self.s18=pygame.image.load('s18.png').convert_alpha()
        self.s19=pygame.image.load('s19.png').convert_alpha()
        self.s20=pygame.image.load('s20.png').convert_alpha()
        self.s21=pygame.image.load('s21.png').convert_alpha()
        self.s22=pygame.image.load('s22.png').convert_alpha()
        self.s23=pygame.image.load('s23.png').convert_alpha()
        self.s24=pygame.image.load('s24.png').convert_alpha()

        if self.ai==False:
            self.image=self.i7
        elif ai1==True:
            self.image=self.s1
        else:
            self.image=self.r1

        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.gravity=0.4
        self.bulldir=True
        self.ret1=ret1
        self.ret2=ret2
        self.stay=False
        self.imagechange=1
        self.imagechange2=1
        self.interval2=0
        self.right=True
        self.rightR=False
        self.shoot=False
        self.imagechangeR=1
        self.imagechange2R=1

    def update(self):

        self.my+=self.gravity


        if self.mx>0:
            self.bulldir=True
        elif self.mx<0:
            self.bulldir=False

        if self.stay == False:
            self.rect.x+=self.mx

        blockhitlist=pygame.sprite.spritecollide(self,self.blockgp,False)
        for block in blockhitlist:
            if self.mx>0:
                self.rect.right=block.rect.left
            elif self.mx<0:
                self.rect.left=block.rect.right

        if self.rect.bottom>=self.winy:
            self.rect.bottom=self.winy
        else:
            self.rect.y+=self.my
            blockhitlist=pygame.sprite.spritecollide(self,self.blockgp,False)
            for block in blockhitlist:
                if self.my>0:
                    self.rect.bottom=block.rect.top
                    self.my=0
                elif self.my<0:
                    self.rect.top=block.rect.bottom
                    self.my=0


        if self.rect.x<=0:
            self.rect.x=0
        if self.rect.right>=900:
            self.rect.right=900

        if self.ai == True:
            self.AI()


    def jump(self):
        self.rect.y+=2
        platformhitlist=pygame.sprite.spritecollide(self,self.blockgp,False)
        self.rect.y-=2
        if len(platformhitlist)>0 or self.rect.bottom>=self.winy:
            self.my=-10
        self.rect.y+=self.my

    def AI(self):
        if self.rect.right>self.ret1:
            self.mx=-self.mx
        elif self.rect.left<self.ret2:
            self.mx=-self.mx

        if self.ai2==True:
            if self.mx<0:
                self.rightR=True
                if self.imagechangeR>=1 and self.imagechangeR<7:
                    self.image=self.r1
                    self.imagechangeR+=1
                elif self.imagechangeR>=7 and self.imagechangeR<14:
                    self.image=self.r2
                    self.imagechangeR+=1
                elif self.imagechangeR>=14 and self.imagechangeR<21:
                    self.image=self.r3
                    self.imagechangeR+=1
                elif self.imagechangeR>=21 and self.imagechangeR<28:
                    self.image=self.r4
                    self.imagechangeR+=1
                elif self.imagechangeR>=28 and self.imagechangeR<35:
                    self.image=self.r5
                    self.imagechangeR+=1
                elif self.imagechangeR>=35:
                    self.image=self.r6
                    self.imagechangeR+=1
                    if self.imagechangeR>42:
                        self.imagechangeR=1

            elif self.mx==0:
                if self.rightR==True:
                    self.image=self.r1
                    self.imagechangeR=1

            if self.mx>0:
                self.rightR=False
                if self.imagechange2R>=1 and self.imagechange2R<7:
                    self.image=self.r7
                    self.imagechange2R+=1
                elif self.imagechange2R>=7 and self.imagechange2R<14:
                    self.image=self.r8
                    self.imagechange2R+=1
                elif self.imagechange2R>=14 and self.imagechange2R<21:
                    self.image=self.r9
                    self.imagechange2R+=1
                elif self.imagechange2R>=21 and self.imagechange2R<28:
                    self.image=self.r10
                    self.imagechange2R+=1
                elif self.imagechange2R>=28 and self.imagechange2R<35:
                    self.image=self.r11
                    self.imagechange2R+=1
                elif self.imagechange2R>=35:
                    self.image=self.r12
                    self.imagechange2R+=1
                    if self.imagechange2R>42:
                        self.imagechange2R=1
            elif self.mx==0:
                if self.rightR==False:
                    self.image=self.r7
                    self.imagechange2R=1


        if self.ai1==True:

            if self.mx>0:
                self.rightR=True
                if self.imagechangeR>=1 and self.imagechangeR<7:
                    self.image=self.s1
                    self.imagechangeR+=1
                elif self.imagechangeR>=7 and self.imagechangeR<14:
                    self.image=self.s3
                    self.imagechangeR+=1
                elif self.imagechangeR>=14 and self.imagechangeR<21:
                    self.image=self.s4
                    self.imagechangeR+=1
                elif self.imagechangeR>=21 and self.imagechangeR<28:
                    self.image=self.s5
                    self.imagechangeR+=1
                elif self.imagechangeR>=28 and self.imagechangeR<35:
                    self.image=self.s6
                    self.imagechangeR+=1
                elif self.imagechangeR>=35 and self.imagechangeR<42:
                    self.image=self.s7
                    self.imagechangeR+=1
                elif self.imagechangeR>=42 and self.imagechangeR<49:
                    self.image=self.s8
                    self.imagechangeR+=1
                elif self.imagechangeR>=49 and self.imagechangeR<56:
                    self.image=self.s9
                    self.imagechangeR+=1
                elif self.imagechangeR>=56 and self.imagechangeR<63:
                    self.image=self.s10
                    self.imagechangeR+=1
                elif self.imagechangeR>=63 and self.imagechangeR<70:
                    self.image=self.s11
                    self.imagechangeR+=1
                elif self.imagechangeR>=70:
                    self.image=self.s12
                    self.imagechangeR+=1
                    if self.imagechangeR>77:
                        self.imagechangeR=1

            elif self.mx==0:
                if self.rightR==True:
                    self.image=self.s1
                    self.imagechangeR=1

            elif self.mx<0:
                self.rightR=False
                if self.imagechangeR>=1 and self.imagechangeR<7:
                    self.image=self.s13
                    self.imagechangeR+=1
                elif self.imagechangeR>=7 and self.imagechangeR<14:
                    self.image=self.s15
                    self.imagechangeR+=1
                elif self.imagechangeR>=14 and self.imagechangeR<21:
                    self.image=self.s16
                    self.imagechangeR+=1
                elif self.imagechangeR>=21 and self.imagechangeR<28:
                    self.image=self.s17
                    self.imagechangeR+=1
                elif self.imagechangeR>=28 and self.imagechangeR<35:
                    self.image=self.s18
                    self.imagechangeR+=1
                elif self.imagechangeR>=35 and self.imagechangeR<42:
                    self.image=self.s19
                    self.imagechangeR+=1
                elif self.imagechangeR>=42 and self.imagechangeR<49:
                    self.image=self.s20
                    self.imagechangeR+=1
                elif self.imagechangeR>=49 and self.imagechangeR<56:
                    self.image=self.s21
                    self.imagechangeR+=1
                elif self.imagechangeR>=56 and self.imagechangeR<63:
                    self.image=self.s22
                    self.imagechangeR+=1
                elif self.imagechangeR>=63 and self.imagechangeR<70:
                    self.image=self.s23
                    self.imagechangeR+=1
                elif self.imagechangeR>=70:
                    self.image=self.s24
                    self.imagechangeR+=1
                    if self.imagechangeR>77:
                        self.imagechangeR=1
            elif self.mx==0:
                if self.rightR==False:
                    self.image=self.s13
                    self.imagechange2R=1

            if self.stay==True:
                if self.rightR==True:
                    if self.player!=False:
                        if self.player.rect.x>self.rect.x and self.mx>0:
                            self.image=self.s1
                        else:
                            self.image=self.s13
                elif self.rightR==False:
                    if self.player!=False:
                        if self.player.rect.x<self.rect.x and self.mx<0:
                            self.image=self.s13
                        else:
                            self.image=self.s1
            if self.aistay==True:
                self.image=self.s13
            elif self.aistay==False:
                self.image=self.s1


    def Animate(self):
        if self.mx>0:
            self.right=True
            if self.imagechange>=1 and self.imagechange<7:
                self.image=self.i1
                self.imagechange+=1
            elif self.imagechange>=7 and self.imagechange<14:
                self.image=self.i2
                self.imagechange+=1
            elif self.imagechange>=14 and self.imagechange<21:
                self.image=self.i3
                self.imagechange+=1
            elif self.imagechange>=21 and self.imagechange<28:
                self.image=self.i4
                self.imagechange+=1
            elif self.imagechange>=28 and self.imagechange<35:
                self.image=self.i5
                self.imagechange+=1
            elif self.imagechange>=35:
                self.image=self.i6
                self.imagechange+=1
                if self.imagechange>42:
                    self.imagechange=1

        elif self.mx==0:
            if self.right==True:
                self.image=self.i7
                self.imagechange=1


        if self.mx<0:
            self.right=False
            if self.imagechange2>=1 and self.imagechange2<7:
                self.image=self.i17
                self.imagechange2+=1
            elif self.imagechange2>=7 and self.imagechange2<14:
                self.image=self.i9
                self.imagechange2+=1
            elif self.imagechange2>=14 and self.imagechange2<21:
                self.image=self.i10
                self.imagechange2+=1
            elif self.imagechange2>=21 and self.imagechange2<28:
                self.image=self.i11
                self.imagechange2+=1
            elif self.imagechange2>=28 and self.imagechange2<35:
                self.image=self.i12
                self.imagechange2+=1
            elif self.imagechange2>=35:
                self.image=self.i13
                self.imagechange2+=1
                if self.imagechange2>42:
                    self.imagechange2=1
        elif self.mx==0:
            if self.right==False:
                self.image=self.i17
                self.imagechange2=1


        if self.my<0:
            if self.right==False:
                self.image=self.i15
            if self.right==True:
                self.image=self.i18

        if self.shoot==True:
            if self.interval2>=0 and self.interval2<10:
                if self.bulldir==True:
                    self.image=self.i8
                else:
                    self.image=self.i16
                self.interval2+=1
            else:
                self.shoot=False
                if self.interval2>9:
                    self.interval2=0


