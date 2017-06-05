import sys
from char import *
from blocks import *
from bullets import *
from levels import *


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
                font=pygame.font.Font(None,40)
                ren=font.render('That\'s it for the demo',True,(0,0,0))
                lvl.window.blit(ren,(lvl.windowX/2-150,lvl.windowY/2-60))
            else:
                font=pygame.font.Font(None,40)
                ren=font.render('Press Enter',True,(0,0,0))
                lvl.window.blit(ren,(lvl.windowX/2-80,lvl.windowY/2-60))
        if level==1:
            font=pygame.font.Font(None,30)
            ren=font.render('Get the key from the enemy',True,(0,0,0))
            lvl.window.blit(ren,(lvl.windowX/2-150,lvl.windowY/2-180))
        if level==2:
            font=pygame.font.Font(None,30)
            ren=font.render('Bullets don\'t penetrate through shields',True,(0,0,0))
            lvl.window.blit(ren,(lvl.windowX/2-200,lvl.windowY/2-250))


        clock.tick(60)
        pygame.display.flip()

Game()