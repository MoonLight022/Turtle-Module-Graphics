from turtle import *
from random import choice
t1 = Turtle()

Screen().bgcolor("black")
Screen().title("Vishnu Lohkna Graphics")
t1.speed(5)
t1.pensize(2)
t1.penup()
t1.goto(-50,-50)
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
	t1.lt(95)
	t1.fd(100)
