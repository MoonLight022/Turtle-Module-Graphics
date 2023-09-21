from turtle import*
import colorsys
bgcolor('black')

hideturtle()
speed(0)
pensize(3)
h = 0
bg = [ 'yellow', 'gold', 'orange', 'red', 'maroon', 'violet', 'magenta', 'purple', 'navy', 'blue', 'skyblue', 'cyan', 'turquoise', 'lightgreen', 'green', 'darkgreen', 'chocolate', 'brown', 'black', 'gray' ]
for i in range(100):
	c = colorsys.hsv_to_rgb(h,1,1)
	pencolor(c)
	#bgcolor(bg[i%len(bg)])
	h+=0.006
	fd(i)
	circle(i, 315)
bgcolor('black')
fd(50)
done()

