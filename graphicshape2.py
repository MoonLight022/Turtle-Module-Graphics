import turtle
import colorsys
t = turtle.Turtle()
turtle.Screen().bgcolor("Black")
t.pensize(2)
t.speed(0)
n,h = 36,0
for i in range(100):
	c = colorsys.hsv_to_rgb(h,1,1)
	h+=1/n
	t.pencolor(c)
	t.fd(i*4)
	t.lt(100)
	t.fd(i*3-20)
	t.lt(200)
	t.rt(20)
turtle.done()
