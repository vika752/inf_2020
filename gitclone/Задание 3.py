#!/usr/bin/env python
# coding: utf-8

# In[1]:


# З А Д А Н И Е   3

import pygame
from pygame.draw import *

pygame.init()
FPS = 30
screen = pygame.display.set_mode((380, 250))
rect(screen, (128,128, 128), (0,0,380,250))
                   #FIRST
#blouse
circle(screen, (150, 120, 45), (120, 270), 60)
circle(screen, (150, 120, 45), (60, 250), 20)
circle(screen, (150, 120, 45), (180, 250), 20)
#head
circle(screen, (209, 159, 113), (120, 170), 50)
#eyes
circle(screen, (113, 209, 124), (100, 160), 10)
circle(screen, (113, 209, 124), (140, 160), 10)
circle(screen, (0, 0, 0), (100, 160), 3)
circle(screen, (0, 0, 0), (140, 160), 3)
#hair
polygon(screen, (0,255,255), ([(120,110),(125,120),(115,120)]))
polygon(screen, (0,255,255), ([(130,115),(125,120),(115,120)]))
polygon(screen, (0,255,255), ([(110,115),(125,120),(115,120)]))
#nose
polygon(screen, (0,255,255), ([(120,160),(125,170),(115,170)]))
#mouth
polygon(screen, (250, 25, 25), ([(120,190),(110,180),(130,180)]))
                  
                  #SECOND
#blouse
circle(screen, (100, 100, 100), (280, 270), 60)
circle(screen, (100, 100, 100), (340, 250), 20)
circle(screen, (100, 100, 100), (220, 250), 20)
#head
circle(screen, (209, 159, 113), (280, 170), 50)
#eyes
circle(screen, (113, 137, 209), (260, 160), 10)
circle(screen, (113, 137, 209), (300, 160), 10)
circle(screen, (0, 0, 0), (260, 160), 3)
circle(screen, (0, 0, 0), (300, 160), 3)
#hair
circle(screen, (0, 0, 0), (260, 118), 8)
circle(screen, (0, 0, 0), (270, 118), 8)
circle(screen, (0, 0, 0), (280, 118), 8)
circle(screen, (0, 0, 0), (290, 118), 8)
#nose
polygon(screen, (0,255,255), ([(280,160),(285,170),(275,170)]))
#mouth
polygon(screen, (250, 25, 25), ([(280,190),(290,180),(270,180)]))

#phrase
rect(screen, (255, 255, 255), (40, 80, 5, 200))
rect(screen, (255, 255, 255), (340, 80, 5, 200))



rect(screen, (255,255,255), (30, 60, 340, 36))
myfont = pygame.font.SysFont('Comic Sans MS', 30)
textsurface = myfont.render('PYTHON is REALLY AMAZING!', False, (0, 0, 0))
screen.blit(textsurface,(45,65))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()




# In[ ]:





# In[ ]:





# In[ ]:




