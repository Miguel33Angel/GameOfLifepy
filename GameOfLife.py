import numpy as np
import time
import math
import pygame, sys
from pygame.locals import *

##CONSTANTES LOGICA
eC=10
size = ancho, altura = 400, 400
nxC=int(ancho/eC)
nyC=int(altura/eC)

gameState=np.zeros((nxC,nyC))
gameState[1][1]=1
gameState[1][2]=1
gameState[1][0]=1

##CONSTANTES PYGAME
WHITE=(255,255,255)
RED = (255, 0 , 0 )
BLACK=( 0 , 0 , 0 )
FPS = 30 # frames per second setting 
ACTUALIZAR=True
#Tracking mouse
mousex, mousey = 0, 0

#EXAMPLE OF polygon
#pygame.draw.polygon(screen, (255,255,255) ,[(50,50),(50,200),(200,200),(200,50)])
#pygame.draw.rect(screen,WHITE,cell)


##PYGAME
pygame.init()
pygame.display.set_caption('Game Of Life') 
screen = pygame.display.set_mode(size=size)
fpsClock = pygame.time.Clock()

##SHOW PAUSED
fontObj = pygame.font.Font('freesansbold.ttf', 32) 
textSurfaceObj = fontObj.render('Pausado', True, WHITE, RED)
textRectObj = textSurfaceObj.get_rect() 
textRectObj.center = (200, 150) 

##SHOW IMAGENES DE CELULAS
DeadImg = pygame.image.load('DEAD.png') 
LiveImg = pygame.image.load('LIVE.png') 
##DISPLAY LOOP
while True:
    screen.fill((0,0,0))

    newState=np.copy(gameState)

    for y in range(nyC):
        for x in range(nxC):
            #LOGICA
            

            n_vivas=gameState[(x - 1) % nxC][(y - 1) % nyC] + \
                gameState[(x - 1) % nxC][(y    ) % nyC] + \
                gameState[(x - 1) % nxC][(y + 1) % nyC] + \
                gameState[(x    ) % nxC][(y - 1) % nyC] + \
                gameState[(x    ) % nxC][(y + 1) % nyC] + \
                gameState[(x + 1) % nxC][(y - 1) % nyC] + \
                gameState[(x + 1) % nxC][(y    ) % nyC] + \
                gameState[(x + 1) % nxC][(y + 1) % nyC]

            if (gameState[x][y]== 0 and n_vivas == 3):
                newState[x][y] = 1
            if(gameState[x][y]== 1 and (n_vivas<2 or n_vivas > 3)):
                newState[x][y] = 0

            #PYGAME
            cell = pygame.Rect(x*eC,y*eC,eC,eC)       #Redefino celula
            if (gameState[x,y]==1):
                screen.blit(LiveImg, (x*eC,y*eC))
                #pygame.draw.rect(screen,WHITE,cell) #Dibujo las que estan vivas
            else:
                screen.blit(DeadImg, (x*eC,y*eC))
                #pygame.draw.rect(screen,WHITE,cell,1) #Dibujo las que estan muertas
            #newState[x][y]=1

    
    #FIN BUCLES CELULAS

    if(ACTUALIZAR):
        gameState=newState
    else:
        screen.blit(textSurfaceObj, textRectObj) 


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            mousex, mousey = event.pos
            cellx=int(mousex/eC)
            celly=int(mousey/eC)
            gameState[cellx, celly]= abs(gameState[cellx, celly]-1)
        elif event.type == KEYDOWN:
            if event.key == K_SPACE:
                ACTUALIZAR=not ACTUALIZAR

            #if event.key == K_q:
    pygame.display.update()
    fpsClock.tick(FPS)
    time.sleep(0.2)

##End Pygame



