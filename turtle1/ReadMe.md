## Introduction
This folder contains some simple examples using Python Turtle to draw various simple graphics.

The software was written on a Windows PC using Python v3.8.1

## PlotCircle
This program shows the basics of using Turtle to draw a static image.

If you take a *point* in a **Cartesian Plane** (eg 2 dimensional graph with x,y axes), let that point be the **"Origin"** (x=0,y=0), then draw a straight line outwards from it - call it the **"radius"**, keep one end of the line **fixed** at the *Origin*, and then sweep the *radius* around through 360 degrees - the other end of the line (not fixed to the Origin), will draw out a ***circle***.

The diagram below demonstrates a radius being drawn along the positive x axis, and then swept around the *Origin* anti-clockwise.

![A radius rotating around an origin, drawing a circle](./images/plotcircle_radius.svg)

Consider the diagram **below**...

The ***radius*** can be seen as the **Hypotenuse** of a triangle.  That triangle can be formed with two sides that are parallel to the **x** and **y** axes of the plane.  The x-axis and y-axis "sides" form a **right-angle triangle** with the *hypotenuse*.

The angle **theta** is the angle relative to the **x-axis** that the **radius** makes, as it sweeps around to form the circle.

The side on the *x* axis, relative to the angle *theta*, is known as the **Adjacent** side (in basic trigonometry.)  Similarly, the side on the *y* axis, is known as the **Opposite** side.

![The radius forms the hypotenuse of a triangle](./images/plotcircle_triangle.svg)

Our basic trigonometry tells us that:

![Formula for x/r](./images/xrfraction.png)

and 

![Formula for x/r](./images/yrfraction.png)

These both now give us values for **x** and **y**, in parametric form using the angle *theta* as the *independent parameter.*