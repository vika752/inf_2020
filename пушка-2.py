#!/usr/bin/env python
# coding: utf-8

# In[5]:


from random import randrange as rnd, choice
import tkinter as tk
import math
import time

print (dir(math))

root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canv = tk.Canvas(root, bg = 'yellow')
canv.pack(fill = tk.BOTH, expand = 1)

        # Constructor of class Ball
class Ball():
    def __init__(self, x = 40, y = 450):
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(['blue', 'green', 'red', 'brown'])
        
        # draws ball
        
        self.id = canv.create_oval(self.x - self.r, self.y - self.r,
                                   self.x + self.r, self.y + self.r, fill = self.color)
        
        self.live = 30

    def set_coords(self):
    
        # sets coords of ball
    
        canv.coords(self.id, self.x - self.r,
                     self.y - self.r, self.x + self.r, self.y + self.r)

    def move(self):
        
        # Moves ball one step in time (Upd self.x and self.y)
 
        self.vy -= 1
        if self.x + self.vx <= 0 or self.x + self.vx >= 800:
            self.vx = -self.vx
        if self.y + self.vy <= 0 or  self.y + self.vy >= 600:
            self.vy = -self.vy  
        self.x += self.vx
        self.y -= self.vy
        if self.live < 0:
            balls.pop(balls.index(self))
            canv.delete(self.id)
        else:
            self.live -= 1
        self.set_coords()

    def hittest(self, obj):
        r_1 = (self.x + self.r - obj.x - obj.r)**2
        r_2 = (self.y + self.r  - obj.y - obj.r)**2
        r_3 = (self.r + obj.r)**2
        condition = r_1 + r_2 <= r_3
        if condition:
            return True
        else:
            return False
 
 #class that describes target       
         
class Target():
    def __init__(self):

        #sets initial characteristics of target
        self.points = 0
        self.live = 1
        self.id = canv.create_oval(0, 0, 0, 0)
        
        # contains number of hitten targets
        self.id_points = canv.create_text(30, 30, text = self.points, font = '28')
 
 #Creates new target 
    def new_target(self):
        x = self.x = rnd(600, 780)
        y = self.y = rnd(300, 550)
        r = self.r = rnd(2, 50)
        self.vx = rnd(-7, 7)
        self.vy = rnd(-7, 7)
        color = self.color = 'green'
        canv.coords(self.id, x - r, y - r, x + r, y + r)
        canv.itemconfig(self.id, fill = color)

    def hit(self, points = 1):
        canv.coords(self.id, -10, -10, -10, -10)
        self.points += points
       
        # writes number of points
        canv.itemconfig(self.id_points, text = self.points)
        
    def check_border(self):
        
       # checks if border was hiiten 
       
        if self.x + self.vx <= 0 or self.x + self.vx >= 800:
            self.vx = -self.vx
        if self.y + self.vy <= 0 or  self.y + self.vy >= 600:
            self.vy = -self.vy
         
      # moves target on one step in time     
    def move(self):
       self.check_border()
       self.x += self.vx
       self.y += self.vy
       canv.coords(self.id, self.x - self.r, self.y - self.r, 
                   self.x + self.r, self.y + self.r)

   
   # class that discribes Gun
class Gun():
   
    def __init__(self, x = 40, y = 450):

        #(x, y in type int)
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        # draws gun
        self.id = canv.create_line(20, 450, 50, 420, width = 9)

    def fire2_start(self, event):
       
        #sets regime of fire (event in type list)
       
        self.f2_on = 1

    def fire2_end(self, event):
        
        #strikes when we push the mouse button (event in type list)
        
        global balls, bullet
        bullet += 1
        new_ball = Ball()
        new_ball.r += 5
        self.an = math.atan((event.y - new_ball.y) / (event.x - new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event = 0):
        if event:
            if event.x - 20 != 0:
                self.an = math.atan((event.y - 450) / (event.x - 20))
        if self.f2_on:
            canv.itemconfig(self.id, fill = 'red')
        else:
            canv.itemconfig(self.id, fill = 'black')
        canv.coords(self.id, 20, 450,
                    20 + max(self.f2_power, 20) * math.cos(self.an),
                    450 + max(self.f2_power, 20) * math.sin(self.an))

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canv.itemconfig(self.id, fill = 'red')
        else:
            canv.itemconfig(self.id, fill = 'black')


t1 = Target()
t2 = Target()
screen1 = canv.create_text(400, 300, text = '', font = '28')
g1 = Gun()
bullet = 0
balls = []

 #creates new game
def new_game(event=''):

    global Gun, t1, t2, screen1, balls, bullet
    t1.new_target()
    t2.new_target()
    bullet = 0
    balls = []
    canv.bind('<Button-1>', g1.fire2_start)
    canv.bind('<ButtonRelease-1>', g1.fire2_end)
    canv.bind('<Motion>', g1.targetting)
    z = 0.03
    t1.live = 1
    t2.live = 1
    while t1.live or t2.live or balls:
        if t1.live > 0:
            t1.move()
        if t2.live > 0:
            t2.move() 
        for b in balls:
            b.move()
            if b.hittest(t1) and t1.live:
                t1.live = 0
                t1.hit()
            elif b.hittest(t2) and t2.live:
                t2.live = 0
                t2.hit()
            elif t1.live == 0 and t2.live == 0:
                canv.itemconfig(screen1, text='Вы уничтожили цели за ' + str(bullet) + ' выстрелов')
                canv.bind('<Button-1>', '') 
                canv.bind('<ButtonRelease-1>', '')
        canv.update()
        time.sleep(0.03)
        g1.targetting()
        g1.power_up()
        canv.delete(balls)
    canv.itemconfig(screen1, text='')
    canv.delete(Gun)
    root.after(750, new_game)


new_game()
root.mainloop()
 


# In[ ]:




