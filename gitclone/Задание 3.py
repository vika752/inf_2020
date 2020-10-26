#!/usr/bin/env python
# coding: utf-8

# In[1]:


# З А Д А Н И Е    3

import pygame
from pygame.draw import *

pygame.init()
FPS = 30
x = 380
y = 250
r = 1
screen = pygame.display.set_mode((x, y))
rect(screen, (128,128, 228), (0, 0, x, y))

BROWN = (150, 120, 45) 
GREY = (100, 100, 100) 
HEAD = (209, 159, 113)
BLUE = (0,255,255)
GREEN = (113, 209, 124)
RED = (250, 25, 25)
DARKBLUE = (113, 137, 209)
BLACK = (0, 0, 0)
                 

colour = [BROWN, GREY, HEAD, BLUE, GREEN, RED, DARKBLUE, BLACK]

def blouse (colour, x, y, r):
    circle(screen, colour[0], (x/3.167, y/0.923), r*60)
    circle(screen, colour[0], (x/6.333+340, y/1), r*20)
    circle(screen, colour[0], (x/2.111+340, y/1), r*20)
    
def nose (colour, x, y):
    polygon(screen, colour[3], ([(x/3.167, y/1.563),(x/3.04, y/1.471),(x/3.304,y/1.471)]))
       
def mouth (colour, x, y):
    polygon(screen, colour[5], ([(x/3.167, y/1.316),(x/3.455, y/1.389),(x/2.923, y/1.389)]))
           
        
def eyes(colour, x, y, r):
    circle(screen, colour[4], (x/3.8, y/1.563), r*10)
    circle(screen, colour[4], (x/2.714, y/1.563), r*10)
    circle(screen, colour[7] , (x/3.8, y/1.563), r*3)
    circle(screen, colour[7], (x/2.714, y/1.563), r*3)
                
def hair1(colour, x, y):
    polygon(screen, colour[3], ([(x/3.167,y/2.273),(x/3.04, y/2.083),(x/3.304, y/2.083)]))
    polygon(screen, colour[3], ([(x/2.923, y/2.174),(x/3.04, y/2.083),(x/3.304, y/2.083)]))
    polygon(screen, colour[3], ([(x/3.455, y/2.174),(x/3.04, y/2),(x/3.304, y/2.083)]))
    
def hair2(colour, x, y, r):
    circle(screen, colour[7], (x/1.462, y/2.119), r*8)
    circle(screen, colour[7], (x/1.407, y/2.119), r*8)
    circle(screen, colour[7], (x/1.357, y/2.119), r*8)
    circle(screen, colour[7], (x/1.31, y/2.119), r*8)
    

def head (colour, x, y, r, a):
    circle(screen, colour[2], (x/3.167, y/1.471), r*50)
    nose(colour, x, y)
    mouth (colour, x, y)
    eyes(colour, x, y, r)
    
    if a == 1:  # colour hair
        hair1(colour, x, y)  
    else:
        hair2(colour, x-420, y, r)
        
        
                        # F I R S T   P E O P L E
  
blouse(colour, x, y, 1)
head(colour, x, y, 1, 1)
                      
                        # S E C O N D  P E O P L E
    
colour = [GREY, BROWN, HEAD, BLUE, DARKBLUE, RED, GREEN, BLACK] 

blouse(colour, x+340, y, 1)
head(colour, x+340, y, 1, 2)
       
    
#phrase
rect(screen, (255, 255, 255), (40, 80, 5, 200))
rect(screen, (255, 255, 255), (340, 80, 5, 200))
#bang
circle(screen, (237, 247, 17), (220, 25), 70)
circle(screen, (247, 233, 17), (220, 25), 50)


#first jet bird
ellipse(screen, (128, 128, 128), (250, 18, 50, 18))
rect(screen, (255, 255, 255), (300, 25, 90, 2))
polygon(screen, (128, 128, 128), ([298, 25], [305, 20], [305, 30]))
circle(screen, (128, 128, 128), (248, 25), 10)
circle(screen, (255, 255, 255), (248, 25), 3)
polygon(screen, (255, 20, 25), ([240, 31], [240, 19], [230, 25]))
ellipse(screen, (128, 128, 128), (265, 20, 15, 30))
#second jet bird
rect(screen, (255, 30, 30), (0, 27, 199, 2))
ellipse(screen, (128, 200, 128), (170, 18, 50, 18))
polygon(screen, (128, 200, 128), ([170, 30], [165, 20], [165, 25]))
circle(screen, (128, 200, 128), (210, 15), 10)
circle(screen, (255, 255, 255), (210, 15), 3)
polygon(screen, (255, 20, 25), ([230, 15], [220, 10], [220, 20]))

#стекло на остановке
s = pygame.Surface((340,360))  # the size of rect
s.set_alpha(128)                
s.fill((255,255,255))           
screen.blit(s, (30,60))    


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

