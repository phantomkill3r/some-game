import pygame,random,sys

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


class Key(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load('key.png')
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y


class WinTile(pygame.sprite.Sprite):
    def __init__(self,x,y,sx=20,sy=40):
        self.sizex=20
        self.sizey=40
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load('arrow.png').convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y

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


class Levels:

    def emptysprites(self):
        self.playergp.empty()
        self.aigp.empty()
        self.blockgp.empty()
        self.bulletgp.empty()
        self.aibulletgp.empty()
        self.keygp.empty()
        self.wintilegp.empty()
        self.spikeblockgp.empty()
        self.grapplegp.empty()


    def variables(self):

        self.windowX=900
        self.windowY=550
        self.window=pygame.display.set_mode((self.windowX,self.windowY))
        self.caption=pygame.display.set_caption('Some Game')
        self.blockgp=pygame.sprite.Group()
        self.spikeblockgp=pygame.sprite.Group()
        self.bulletgp=pygame.sprite.Group()
        self.grapplegp=pygame.sprite.Group()
        self.aibulletgp=pygame.sprite.Group()
        self.interval1,self.interval2=0,0
        self.ai1kill=False
        self.ai2kill=False
        self.playerkill=False
        self.keygp=pygame.sprite.Group()
        self.lvlclear=''
        self.wintilegp=pygame.sprite.Group()
        self.nextlevel=False
        self.interval3=0
        self.arrow=False


    def LvlLoop(self):

        pygame.sprite.groupcollide(self.aigp,self.playergp,False,True)

        pygame.sprite.groupcollide(self.playergp,self.spikeblockgp,True,False)
        if pygame.sprite.groupcollide(self.playergp,self.spikeblockgp,True,False):
            self.playerkill=True

        if self.ai1kill==False:
            enemyhitlist=pygame.sprite.spritecollide(self.ai1,self.bulletgp,True)
            if enemyhitlist:
                self.aigp.remove(self.ai1)
                if self.keyholder=='ai1':
                    self.key=Key(self.ai1.rect.x,self.ai1.rect.y)
                    self.keygp.add(self.key)
                    del self.ai1
                    self.lvlclear=False
                self.ai1kill=True

        if self.ai2kill==False:
            enemyhitlist=pygame.sprite.spritecollide(self.ai2,self.bulletgp,True)
            for bullet in enemyhitlist:
                if bullet.mx>0 and self.ai2.mx>0 or bullet.mx<0 and self.ai2.mx<0:
                    if enemyhitlist:
                        self.aigp.remove(self.ai2)
                        self.bulletgp.remove(bullet)
                        if self.keyholder=='ai2':
                            self.key=Key(self.ai2.rect.x,self.ai2.rect.y)
                            self.keygp.add(self.key)
                            del self.ai2
                            self.lvlclear=False
                        self.ai2kill=True



        pygame.sprite.groupcollide(self.playergp,self.keygp,False,True)

        if self.lvlclear==False:
            if len(self.keygp)==0:
                if pygame.sprite.groupcollide(self.playergp,self.wintilegp,False,False):
                    self.emptysprites()
                    self.nextlevel=True


        pygame.sprite.groupcollide(self.aibulletgp,self.playergp,True,True)
        if len(self.playergp)==0:
            self.playerkill=True
        if self.playerkill==True:
            self.bulletgp.empty()

        pygame.sprite.groupcollide(self.bulletgp,self.blockgp,True,False)


        self.interval1=pygame.time.get_ticks()/1000
        if self.interval1>0 and self.interval2==0:
            self.interval2=self.interval1
        if self.ai1kill==False:
            if self.interval1>self.interval2:
                if self.ai1.rect.y+self.ai1.sy>=self.player.rect.y>=self.ai1.rect.y or self.ai1.rect.y+self.ai1.sy>=self.player.rect.y>=self.ai1.rect.y or self.ai1.rect.y+self.ai1.sy>=self.player.rect.y+self.player.sy>=self.ai1.rect.y or self.ai1.rect.y+self.ai1.sy>=self.player.rect.y+self.player.sy>=self.ai1.rect.y:
                    self.aibullet=Bullets(15)
                    self.interval2+=0.5
                    self.ai1.stay=True
                else:
                    self.ai1.stay=False
                    self.interval2+=0.1
        elif self.ai1kill==True:
            self.interval2+=0.1
            try:
                del self.aibullet
            except:
                pass


        try:
            if self.player.rect.x>self.ai1.rect.x:
                self.aibullet.mx=self.aibullet.speed
            elif self.player.rect.x<self.ai1.rect.x:
                self.aibullet.mx=-self.aibullet.speed
            self.aibullet.rect.x=self.ai1.rect.x+32
            self.aibullet.rect.y=self.ai1.rect.y+12
            self.aibulletgp.add(self.aibullet)
        except:
            pass



        for bullet in self.bulletgp:
            if bullet.rect.x>self.windowX or bullet.rect.x<0:
               self.bulletgp.remove(bullet)

        for bullet in self.aibulletgp:
            if bullet.rect.x>self.windowX or bullet.rect.x<0:
                self.aibulletgp.remove(bullet)


        self.player.Animate()
        self.aibulletgp.update()
        self.playergp.update()
        self.aigp.update()
        self.bulletgp.update()
        self.blockgp.update()
        self.grapplegp.update()

        self.wintilegp.draw(self.window)
        self.playergp.draw(self.window)
        self.blockgp.draw(self.window)
        self.bulletgp.draw(self.window)
        self.aibulletgp.draw(self.window)
        self.aigp.draw(self.window)
        self.keygp.draw(self.window)
        self.spikeblockgp.draw(self.window)
        self.grapplegp.draw(self.window)



    def Lvl1(self):

        self.variables()
        self.background=pygame.image.load('bg1.png').convert()

        self.ai2kill=True

        lst=['ai1']
        self.keyholder=random.choice(lst)

        self.playergp=pygame.sprite.Group()
        self.player=CHAR(self.blockgp,winy=self.windowY,y=400)
        self.playergp.add(self.player)

        self.ai1=CHAR(self.blockgp,winy=self.windowY,mx=4,ai=True,ret1=600,ret2=200,x=350,y=300,ai1=True,player=self.player)
        self.aigp=pygame.sprite.Group()
        self.aigp.add(self.ai1)

        for i in range(200,600,30):
            self.block=Block(i,410,level1=True)
            self.blockgp.add(self.block)

        self.wintile=WinTile(800,450,40,80)
        self.wintilegp.add(self.wintile)

    def Lvl2(self):

        self.variables()
        self.background=pygame.image.load('bg2.png').convert()

        self.ai1kill=True
        self.ai2kill=False

        lst=['ai2']
        self.keyholder=random.choice(lst)

        self.playergp=pygame.sprite.Group()
        self.player=CHAR(self.blockgp,winy=self.windowY,y=400)
        self.playergp.add(self.player)

        self.ai2=CHAR(self.blockgp,winy=self.windowY,mx=-5*1.75,ai=True,ret1=899,ret2=1,x=500,y=460,ai2=True)
        self.aigp=pygame.sprite.Group()
        self.aigp.add(self.ai2)


        for i in range(500,700,30):
            self.block=Block(i,410,level2=True)
            self.blockgp.add(self.block)

        for i in range(200,250,30):
            self.movingblock=Block(i,270,3,380,100,level2=True)
            self.blockgp.add(self.movingblock)

        for i in range(500,900,30):
            self.block=Block(i,130,level2=True)
            self.blockgp.add(self.block)

        self.wintile=WinTile(800,130-80,40,80)
        self.wintilegp.add(self.wintile)


    def Lvl3(self):

        self.variables()
        self.background=pygame.image.load('bg3.png').convert()

        self.ai2kill=False
        self.ai1kill=False

        lst=['ai1','ai2']
        self.keyholder=random.choice(lst)


        for i in range(210,900,30):
            self.spikeblock=Block(i,520,spikes=True)
            self.spikeblockgp.add(self.spikeblock)

        for i in range(0,300,30):
            self.block=Block(i,270,level3=True)
            self.blockgp.add(self.block)

        for i in range(0,500,30):
            self.block=Block(i,150,level3=True)
            self.blockgp.add(self.block)

        for i in range(600,650,30):
            self.block=Block(i,270,level3=True)
            self.blockgp.add(self.block)

        for i in range(200,250,30):
            self.movingblock=Block(i,410,3,480,190,level3=True)
            self.blockgp.add(self.movingblock)



        self.playergp=pygame.sprite.Group()
        self.player=CHAR(self.blockgp,winy=self.windowY,y=400)
        self.playergp.add(self.player)


        self.ai1=CHAR(self.blockgp,winy=self.windowY,ai=True,ret1=600,ret2=200,x=250,y=190,ai1=True,player=self.player)
        self.aigp=pygame.sprite.Group()
        self.aigp.add(self.ai1)

        self.ai2=CHAR(self.blockgp,winy=self.windowY,ai=True,ret1=500,ret2=1,x=250,y=10,mx=5*1.75,ai2=True)
        self.aigp.add(self.ai2)

        self.wintile=WinTile(0,150-80,40,80)
        self.wintilegp.add(self.wintile)
        self.wintile.image=pygame.transform.flip(self.wintile.image,True,False)


    def Lvl4(self):

        self.variables()

        self.ai1kill=True
        self.ai2kill=True


        self.playergp=pygame.sprite.Group()
        self.player=CHAR(self.blockgp,winy=self.windowY,y=460)
        self.playergp.add(self.player)


        for i in range(100,300,30):
            self.grapple=Grapple(i,420,self.player,self.grapplegp,100,280)
            self.grapplegp.add(self.grapple)

        self.block=Block(70,420)
        self.blockgp.add(self.block)

        self.block=Block(310,420)
        self.blockgp.add(self.block)

        self.aigp=pygame.sprite.Group()


lvl=Levels()

level=1

def Game():
    global level

    pygame.init()

    clock=pygame.time.Clock()

    if level==1:
        lvl.Lvl1()
    elif level==2:
        lvl.Lvl2()
    elif level==3:
        lvl.Lvl3()

    while True:

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    lvl.player.jump()
                if event.key==pygame.K_RIGHT:
                    lvl.player.mx=5
                if event.key==pygame.K_LEFT:
                    lvl.player.mx=-5
                if event.key==pygame.K_SPACE:
                    lvl.player.shoot=True
                    lvl.bullet=Bullets()
                    if lvl.player.bulldir==True:
                        lvl.bullet.mx=10
                        lvl.bullet.rect.x=lvl.player.rect.x+30
                        lvl.bullet.rect.y=lvl.player.rect.y+30
                    else:
                        lvl.bullet.mx=-10
                        lvl.bullet.rect.x=lvl.player.rect.x
                        lvl.bullet.rect.y=lvl.player.rect.y+30


                    lvl.bulletgp.add(lvl.bullet)
                if event.key==pygame.K_RETURN:
                    if lvl.nextlevel==True:
                        if level==3:
                            level=1
                        else:
                            level+=1
                        Game()
                    if lvl.playerkill==True:
                        Game()


            elif event.type==pygame.KEYUP:
                if event.key==pygame.K_RIGHT:
                    lvl.player.mx=0
                if event.key==pygame.K_LEFT:
                    lvl.player.mx=0
                if event.key==pygame.K_SPACE:
                    lvl.player.shoot=False


        lvl.window.fill((255,255,255))
        lvl.window.blit(lvl.background,(0,0))

        lvl.LvlLoop()

        if lvl.playerkill==True or lvl.nextlevel==True:
            if level==3 and lvl.nextlevel==True:
                font=pygame.font.SysFont('Comic Sans MS',30)
                ren=font.render('That\'s it for the demo',True,(0,0,0))
                lvl.window.blit(ren,(lvl.windowX/2-150,lvl.windowY/2-60))
            else:
                font=pygame.font.SysFont('Comic Sans MS',30)
                ren=font.render('Press Enter',True,(0,0,0))
                lvl.window.blit(ren,(lvl.windowX/2-80,lvl.windowY/2-60))
        if level==1:
            font=pygame.font.SysFont('Comic Sans MS',20)
            ren=font.render('Get the key from the enemy',True,(0,0,0))
            lvl.window.blit(ren,(lvl.windowX/2-150,lvl.windowY/2-180))
        if level==2:
            font=pygame.font.SysFont('Comic Sans MS',20)
            ren=font.render('Bullets don\'t penetrate through shields',True,(0,0,0))
            lvl.window.blit(ren,(lvl.windowX/2-200,lvl.windowY/2-250))


        clock.tick(60)
        pygame.display.flip()

Game()
