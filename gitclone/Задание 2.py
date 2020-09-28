#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# З А Д А Н И Е   2

import pygame
from pygame.draw import *

pygame.init()
FPS = 50
screen = pygame.display.set_mode((450, 450))
#head
rect(screen, (128,128, 128), (0,0,450,450))
ellipse(screen, (237, 202, 242),(150,125,150,200))
#eyebrow
rect(screen, (0, 255, 255), (190, 177, 75 ,3))
#part of the eyes 1
arc(screen, (0, 0, 0), (175, 185, 50, 28),3.84, 0)
arc(screen, (0, 0, 0), (235, 185, 50, 28),3.84, 0)
#eyelids
rect(screen, (0,0,0), (175,195,50,1))
rect(screen, (0,0,0), (235,195,50,1))
#part of the eyes 2
circle(screen, (0, 0, 0), (210, 200), 2)
circle(screen, (0, 0, 0), (265, 200), 2)
#hair
polygon(screen, (0,255,255), ([(150,200),(145,150),(165,170)]))
polygon(screen, (0,255,255), ([(165,170),(150,110),(190,150)]))
polygon(screen, (0,255,255), ([(184,140),(200,70),(225,125)]))
polygon(screen, (0,255,255), ([(225,125),(263,73),(275,140)]))
polygon(screen, (0,255,255), ([(260,137),(285,110),(280,160)]))
#nose
arc(screen, (0,0,0), (225, 195, 10, 60), 3.84, 0 )
#mouth
arc(screen,(0,0,0),(200,275,25,5), 0, 3.14)
#blouse
polygon(screen, (255, 255, 255), ([150, 450], [200, 325], [250, 325], [300, 450]))
#phrase
circle(screen, (255,255,255), (325,225), 15)
circle(screen, (255,255,255), (300,250), 10)
circle(screen, (255,255,255), (330,180), 20)
circle(screen, (255,255,255), (345,115), 24)
rect(screen, (255,255,255), (215,26,220,36))

myfont = pygame.font.SysFont('Comic Sans MS', 30)
textsurface = myfont.render('PYTHON is AMAZING', False, (0, 0, 0))
screen.blit(textsurface,(220,40))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()


