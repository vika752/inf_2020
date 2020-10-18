#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pygame
import pygame.draw
from random import randint
pygame.init()
font = pygame.font.Font(None, 50)

FPS = 50
width = 1000
length = 500
# creating display
screen = pygame.display.set_mode((width, length))
name = input('Your name: ')

# cortege of colors that used in the picture
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
    

class Target:
    def __init__(self, screen, width, length):
        self.x = randint(100, width)
        self.y = randint(100, length)
        self.screen = screen
        self.v_x = randint(-3, 3)
        self.v_y = randint(-3, 3)
        self.rect = (self.x, self.y)
        self.score = randint(1, 5)
        
    
    def move(self):
        self.x += self.v_x
        self.y += self.v_y
        self.rect = (self.x, self.y)
        
        
    def check_border(self, width, length):
        if self.x + self.v_x <= 0 or self.x + self.v_x >= width:
            self.v_x = -self.v_x
        if self.y + self.v_y <= 0 or  self.y + self.v_y >= length:
            self.v_y = -self.v_y
        

# class that consists of functions for creting our objects
class Pictures(Target):
    def __init__(self, screen, width, length):
        '''
        creates our objects, their motion
        and their initial state
        '''
        super().__init__(screen, width, length)
        if randint(0, 1):
            self.image = pygame.image.load('2.png')
            self.coefficient = 2
        else:
            self.image = pygame.image.load('4.png')
            self.coefficient = 1 
        self.rect = self.image.get_rect()
        self.scal = randint(40, 60)
        self.image = pygame.transform.scale(self.image, (self.scal, self.scal))
        
        
    def draw(self):
        screen.blit(self.image, self.rect)
    
    
    def check_event(self, coords):
        '''
        coords in type list
        determines if we hit the object
        '''
        x_m, y_m = coords
        if x_m >= self.x and x_m <= self.x + self.scal:
            condition_x = True
        else:
            condition_x = False
        if self.y <= y_m and self.y + self.scal >= y_m:
            condition_y = True
        else:
            condition_y = False
        if  condition_x and condition_y:
            return True
        else:
            return False

            
class Ball(Target):
    def __init__(self, screen, width, length):
        super().__init__(screen, width, length)
        self.r = randint(10, 99)
        self.color = COLORS[randint(0, 5)]
        
        
    def draw(self):
        ellps = pygame.draw.ellipse(self.screen, self.color, [self.x, self.y, self.r, self.r])

        
    def check_event(self, coords):
        x_m, y_m = coords
        if (self.x - x_m)**2 + (self.y - y_m)**2 <= self.r**2:
            return True
        else:
            return False


class Square(Target):
    def __init__(self, screen, width, length):
        super().__init__(screen, width, length)
        self.r = randint(10, 99)
        self.color = COLORS[randint(0, 5)]
        
        
    def draw(self):
        rectangle = pygame.draw.rect(self.screen, self.color, [self.x - self.r/2, 
                                              self.y - self.r/2, 
                                              self.r, self.r])
        
    def check_event(self, coords):
        x_m, y_m = coords
        if (self.x - x_m)**2 + (self.y - y_m)**2 <= self.r**2:
            return True
        else:
            return False  
            
            
def score(Score):
    '''
    Score - score of the person who pushes the mousebotton
    in type int
    prints score on the picture
    '''
    text = font.render("Score: " + str(Score), True, BLUE)
    screen.blit(text, (100, 100))


clock = pygame.time.Clock()
finished = False
Score =  0 

balls = [Ball(screen, width, length) for i in range(10)] 
squares = [Square(screen, width, length) for i in range(10)]
pictures = [Pictures(screen, width, length) for i in range(10)]
# we create more objects that can disappear
# and we get different number of points for each of them
while not finished:
    clock.tick(FPS)
    screen.fill(WHITE)
    for ball in balls:
        ball.check_border(width, length) 
        for i in balls:
            for j in balls:
                if i!= j:
                    condition_xb = i.x + 2*i.r > j.x and j.x + 2*j.r > i.x
                    condition_yb = i.y + 2*i.r > j.y and j.y + 2*j.r > i.y
                    if condition_xb and condition_yb:
                        i.v_x = -i.v_x
                        i.v_y = -i.v_y
                        j.v_x = -j.v_x
                        j.v_y = -j.v_y                        
        ball.move()
        ball.draw()
    for square in squares:
        square.check_border(width, length) 
        square.move()
        square.draw()
    for picture in pictures:
        picture.check_border(width, length) 
        picture.move()
        picture.draw() 
    score(Score)        
       
                     
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for i, ball in enumerate(balls):
                if ball.check_event(event.pos):
                    Score += ball.score
                    balls.pop(i)
                    balls.append(Ball(screen, width, length))
            for i, square in enumerate(squares):
                if square.check_event(event.pos):
                    Score += square.score
                    squares.pop(i)
                    squares.append(Square(screen, width, length))  
            for i, picture in enumerate(pictures):
                if picture.check_event(event.pos):
                    Score += picture.score
                    pictures.pop(i)
                    pictures.append(Pictures(screen, width, length))                    

                    # writing number of points of a players in file                   
file = open("out.txt", "a")
file.write('Name:' + name + ': ' + str(Score) + '\n')
    
pygame.quit()

