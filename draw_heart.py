import turtle
from random import random
from tkinter import Button

turtle.bgcolor((0, 0, 0))
turtle.pensize(2)
turtle.title('I love you')

run = True


def curve():
	for i in range(200):
		turtle.right(1)
		turtle.forward(1)


def forw():
	for i in range(111):
		turtle.forward(1)


turtle.speed(10)

colour = (0, 0, 0)


def choose_colour():
	global colour
	red = random()
	green = random()
	blue = random()
	colour = (red, green, blue)


def draw():
	global run
	run = True
	while run:
		choose_colour()

		turtle.color(colour, colour)
		turtle.hideturtle()

		turtle.begin_fill()
		turtle.left(140)
		forw()
		# turtle.forward(111.65)
		curve()

		turtle.left(120)
		curve()
		forw()
		# turtle.forward(111.65)
		turtle.end_fill()
		turtle.left(140)


def stop_draw():
	global run
	run = False


def main():
	Button(text="Draw", bg='#000F10', fg='violet', activebackground='violet', width=12, height=2, command=draw).place(x=310, y=350)
	Button(text="Stop", bg='#000F10', fg='violet', activebackground='violet', width=12, height=2, command=stop_draw).place(x=310, y=400)


if __name__ == "__main__":
	main()
	turtle.mainloop()
