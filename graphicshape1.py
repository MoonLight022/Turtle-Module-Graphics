from turtle import *
from random import choice
t1 = Turtle()

Screen().bgcolor("black")
Screen().title("Vishnu Lohkna Graphics")
t1.speed(0)
t1.pensize(2)
t1.penup()
t1.goto(0,-200)
t1.pendown()

#colour = [ 'yellow', 'gold', 'orange', 'red', 'maroon', 'violet', 'magenta', 'purple', 'navy', 'blue', 'skyblue', 'cyan', 'turquoise', 'lightgreen', 'green', 'darkgreen', 'chocolate', 'brown', 'black', 'gray' ]
x,y,z=0,15,30
colormode(255)

for i in range(120):
	"""if x>=255: x=30	
	if y>=255: y=0
	if z>=255: z=15
	x+=5"""
	#t1.pencolor(choice(colour))
	"""t1.pencolor(x,y,z)"""
	t1.pencolor('green')	
	t1.fd(100)
	t1.lt(55)
	t1.fd(100)

'''for i in range(120):
	t1.pencolor('navy')	
	t1.fd(101)
	t1.lt(55)
	t1.fd(150)'''
t1.penup()
t1.goto(220,-110)
t1.pendown()
t1.rt(55)
for i in range(120):
	t1.pencolor('white')	
	t1.fd(125)
	t1.lt(55)
	t1.fd(125)

t1.penup()
t1.goto(-23,277)
t1.pendown()

for i in range(120):
	t1.pencolor('orange')	
	t1.fd(150)
	t1.lt(55)
	t1.fd(150)
done()
