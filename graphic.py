import turtle 
import random
wn=turtle.Screen().bgcolor("black")
colors = ['orange', 'orange', 'orange', 'white', 'white', 'green','green','green'] 
t=turtle.Turtle() 
t.speed(30)
for i in range(36):
    choice=random.choice(colors)
    t.pencolor(choice)
    t.forward(100)
    for _ in range(5): 
        t.forward(30) 
        t.right(360/5) 
    t.penup()
    t.goto(0,0)
    t.pendown()
    t.right(10)

t.penup()
t.goto(0,-100)
t.pendown()
for i in range(50): 
    t.pencolor('white')
    t.circle(100+i, 45)

t.penup()
t.goto(0,0)
t.pendown()

for i in range(36):
    choice=random.choice(colors)
    t.pencolor(choice)
    t.forward(170)
    for _ in range(3): 
        t.forward(45) 
        t.right(360/3) 
    t.penup()
    t.goto(0,0)
    t.pendown()
    t.right(10)

t.penup()
t.goto(170,0)
t.pendown()
for i in range(50): 
    t.pencolor('orange')
    t.circle(170+i, 45)
turtle.done()
