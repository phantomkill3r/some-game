import pygame,random
from char import *
from blocks import *
from bullets import *
from wintile import *
from Grapple import *

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
