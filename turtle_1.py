from turtle import *

# НАСТРОЙКА ЧЕРЕПАШКИ
speed(0.1)


#ОПРЕДЛЕНИЕ КОММАНД

def talloval(r):               # Verticle Oval
    left(45)
    for loop in range(2):      # Draws 2 halves of ellipse
        circle(r,90)    # Long curved part
        circle(r/2,90)  # Short curved part

def flatoval(r, color="green"):               # Horizontal Oval
    right(45)
    fillcolor(color)
    begin_fill()
    for loop in range(2):
        circle(r,90)
        circle(r/2,90)
    end_fill()
    
def draw_center(size, color='yellow'):
    fillcolor(color)
    begin_fill()
    circle(size)
    end_fill()

def flower(size,color):
    for i in range(8):
        flatoval(size,color)
        left(90)
    
    right(90)
    forward(size*4)
    left(180)
    # draw_center()
    forward(size*2)
    left(90)
    flatoval(size/3)
    left(135)
    forward(size/4)
    left(90)
    flatoval(size/3)
    right(45)
    penup()
    left(90)
    forward(size * 3.5)
    left(90)
    forward(size * 2.25)
    right(90)
    pendown()
        


#НАЧАЛО ПРОГРАММЫ


screensize(4000,2000)
penup()
left(180)
forward(400)
right(180)
pendown()

flowers = [[50,"red"], 
           [50,"green"], 
           [50, "blue"], 
           [50,"orange"], 
           [50,"purple"]]

for size, color in flowers:
    flower(size, color)
done()