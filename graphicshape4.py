import turtle
import colorsys
t = turtle.Turtle()
turtle.Screen().bgcolor("Black")
t.pensize(3)
t.speed(0)
t.hideturtle()
n,h = 36,0

# Vid2
"""for i in range(150):
	c = colorsys.hsv_to_rgb(h,1,1)
	h+=0.006
	t.pencolor(c)
	t.fd(i)
	t.circle(10+i)
	t.rt(90)"""

# Vid2
"""for i in range(200):
	c = colorsys.hsv_to_rgb(h,1,1)
	h+=0.006
	t.pencolor(c)
	for j in range(3):
		t.rt(90)
		t.fd(j+i)
		t.circle(50)
		t.rt(70)
	t.circle(20, 4)	
	t.rt(90)"""

# Vid3
"""for i in range(500):
	c = colorsys.hsv_to_rgb(h,1,1)
	h+=0.006
	t.pencolor(c)
	t.fd(i)
	t.circle(10)
	t.rt(70)"""

# Vid4

for i in range(400):
	c = colorsys.hsv_to_rgb(h,1,1)
	h+=0.009
	t.pencolor(c)
	t.fd(i)
	t.circle(10, 4)
	t.rt(100)

turtle.done()
