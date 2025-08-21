#!/usr/bin/env python3
# File: spincircle.py
# Version: 0.2, 21-Aug-2025
# Author: Bill Teluk
# Description:
# Spin Circle in 3D

from turtle import *
#from math import *
import math as m
import time

#fSLOW = Truen
fSLOW = False

clearscreen()
hideturtle()
colormode(1.0)
update()
if not fSLOW:
	tracer(0)

# Circle radius
radius = 200.0
alpha = 0.0 # Spin angle
step =  m.pi / 180 # Angle step for spin and plotting circle
# Step through spin angles
while True: # spin forever
	# Draw circle at this angle
	tracer(0)
	clear() # Clear the previous circle
	begin_fill()
	lrf = abs(m.cos(alpha)) # light reflectance factor
	# Flip colour when coin on edge
	if m.pi / 2 < ( alpha % (2 * m.pi )) < 3 * m.pi / 2:
		color(lrf*1,lrf*0.25,lrf*0.25)
	else:
		color(lrf*0.25,lrf*1,lrf*0.25)
	theta = 0.0
	# Goto initial position
	penup()
	x = int(radius * m.cos(0.0))
	y = int(radius * m.sin(0.0))
	goto(x, y)
	pendown()
	# draw the circle
	while theta <= 2.0 * m.pi:
		x = int(radius * m.cos(theta))
		y = int(radius * m.sin(theta) * m.cos(alpha))
		goto(x, y)
		theta += step
	end_fill()
	penup()
	update()
	#Delay
	time.sleep(0.02)
	alpha += step
	print('Spin at %3.0f' % (alpha * 180 / m.pi))

penup()
if not fSLOW:
	update()

if False:
	while True:
		pass
mainloop()


