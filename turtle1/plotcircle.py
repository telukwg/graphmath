#!/usr/bin/env python3
# File: plotcircle.py
# Version: 0.2, 12-Mar-2024
# Author: Bill Teluk
# Description:
# Plot a Circle using Turtle Graphics
# This program is using a parametric equation for plotting the circle
# It calculates the x,y coordinates to plot the circle using
# an angle and a radius that describes a point moving around the
# edge of a circle.  The radius remains constant, the angle
# changes.  Using the trigonometry functions sine and cosine,
# the program calculates the position of a hypotenuse of a 
# triangle.  The angle of interest is at the centre of the plot,
# the "Adjacent side" of the triangle starts from the centre and
# is parallel to the x-axis (positive or negative), and from the
# end of the "Adjacent side", a line is then plotted upwards or
# downwards, parallel to the y-axis, to form the "Opposite side".
# The length of the adjacent side = x axis offset = r * cos(angle)
# The length of the opposite side = y axis offset = r * sin(angle)
# Only the point at the end of the triangle hypotenuse is plotted,
# this point is on the circle, since it is at a distance from
# from the origin, set by the "radius" value.

from turtle import *
import math as m

response = input('Slow? (Y/N): ')
fSLOW = False
if response[0] in ('Yy'):
	fSLOW = True

response = input('Fill circle? (Y/N): ')
fFILL = False
if response[0] in ('Yy'):
	fFILL = True

# Graphics initialisation
clearscreen() # reset and clear
hideturtle() # hide the turtle/pointer symbol
# Set colours to be in range 0.0 to 1.0
colormode(1.0)
color(1,0.25,0.25) # set colour to be light red pen
if not fSLOW:
	tracer(0) # turn off the drawing delay

# Circle radius
radius = 200.0
# Angle step for plotting the circle, in radians
step =  m.pi / 180 # 1 degree increments
if fFILL: begin_fill()
theta = 0.0 # Angle to start from, in radians
# Goto initial position
penup() # don't draw whilst moving pen to start position
x = int(radius * m.cos(0.0))
y = int(radius * m.sin(0.0))
goto(x, y)
pendown() # put pen down ready to draw
# Draw the circle
while theta <= 2.0 * m.pi:
	# Calculate the next target x, y coordinates given current angle
	x = int(radius * m.cos(theta))
	y = int(radius * m.sin(theta))
	# Draw line from current position to target coordinates
	goto(x, y)
	# Increase the angle to calculate the next point
	theta += step
if fFILL: end_fill()
penup()
if not fSLOW:
	update() # update the screen display with all drawing actions
# Call to keep the graphics display window open
mainloop()