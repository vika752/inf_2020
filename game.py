#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pygame
from pygame.draw import *
from random import randint

pygame.init()
name = input('What is your name?: ')
pygame.display.set_caption('catch Vincent Puh')#имя окна

class Puh(pygame.sprite.Sprite):  #объект-картинка sprite
    def __init__(s):
        pygame.sprite.Sprite.__init__(s)
        
        #изображения
        type = str(randint(1, 4))
        s.image = pygame.image.load(type + '.png')
        s.image.set_colorkey((255, 255, 255))
        
        s.r = (randint(70, 200))
        s.image = pygame.transform.scale(s.image, (s.r, s.r))
        s.rect = s.image.get_rect()
        s.rect.x = randint(100, 1100)
        s.rect.y = randint(100, 600)
        s.vx = randint(-1, 1)
        s.vy = randint(-1, 1)
        s.time = randint(150, 250)
        
        if type == 1 or type == 4:
            s.count = s.vx ** 2 + s.vy ** 2
        else:
            s.count = s.vx ** 2 * 2 + s.vy ** 2 * 2
            
 #от стены
    def update(s):
        s.rect.x += s.vx
        s.rect.y += s.vy
        if s.rect.x < 0 or s.rect.x > 1301 - s.r:
            s.vx = - s.vx
        if s.rect.y < 0 or s.rect.y > 801 - s.r:
            s.vy = - s.vy
        if randint(1, s.time) == 1:
            s.kill()

    def ret(s):
        return s.count

    def click(s, p):
        x = p[0]
        y = p[1]
        o1 = (x - s.rect.x - s.r / 2)
        o2 = (y - s.rect.y - s.r / 2)
        if o1 ** 2 + o2 ** 2 < s.r ** 2 / 4:
            return True
        else:
            return False

            

            
FPS = 50
screen = pygame.display.set_mode((1300, 800))
ballss = pygame.sprite.Group()
clock = pygame.time.Clock()


            
ball = Puh()
ballss.add(ball)
ballss.update()
pygame.display.flip()
fin = False
count = 0
            
            
while not fin:
    clock.tick(FPS)
    screen.fill((105, 255, 105))
    text_score = pygame.font.Font(None, 70)
    text = text_score.render('SCORE:  ' + str(count), 1, (255, 255, 255))
    screen.blit(text, (10, 50))
    ballss.update()
    ballss.draw(screen)
    pygame.display.flip()
    
    if randint(0, 30) == 1:
        ball = Puh()
        ballss.add(ball)
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fin = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            
            for i in ballss:
                if i.click(event.pos):
                    count += i.ret()
                    i.kill()
            
            
score1 = ()
try:
    file = open('results.txt')
    
    for m in file:
        score1.append(m)
    file.close()
    file = open('results.txt', 'w')
    
    score1.append(name + str(count) + '/n')
    
    for i in score1:
        file.write(i)
    file.close()
except:
    file = open('results.txt', 'w')
    
    for i in score1:
        file.write(i)
    file.write(name + ':' + str(count) + '/n')
    file.close()
   
      
    
pygame.quit()


# In[ ]:





# In[ ]:




