import turtle
import math
from math import *
from turtle import *


try:
    tt = turtle.Turtle()
except:
    tt = turtle.Turtle() 
    
ts = turtle.Screen()


length = ts.numinput("Dimensions", "Length")
width = ts.numinput("Dimensions", "Width")
height = ts.numinput("Dimensions", "Height")

angle1 = math.degrees(math.atan(length/width))
angle3 = math.degrees(math.atan(width/length))
angle2 = 180 - (2*angle3)
angle4 = 180 - (2*angle1)

llx = (height + (width/2))*-1
lly = (height + (length/2))*-1
urx = -llx * + length
ury = -lly * + width

flap1 = height

triangles = (((width/2)**2)+((length/2)**2))**0.5

triangles2 = (((width/2)**2)+((length/2)**2))**0.5

#ts.reset()
#ts.setworldcoordinates(-120, -180, 420, 270)

tt.speed(10)

##Center Box
tt.forward(length)

tt.left(90)

tt.forward(width)

tt.left(90)

tt.forward(length)

tt.left(90)

tt.forward(width)

##Height boxes
tt.color('red')

tt.forward(height)

tt.color('black')

tt.left(90)

tt.forward(length)

tt.color('red')

tt.left(90)

tt.forward(height)

tt.color('black')

tt.right(90)

tt.forward(height)

tt.left(90)

tt.forward(width)

tt.left(90)

tt.forward(height)

tt.right(90)

tt.color('red')

tt.forward(height)

tt.color('black')

tt.left(90)

tt.forward(length)

tt.color('red')

tt.left(90)

tt.forward(height)

tt.color('black')

tt.right(90)

tt.forward(height)

tt.left(90)

tt.forward(width)

tt.left(90)

tt.forward(height)

##Flaps and Triangles
tt.color('red')

#Triangle 1
tt.right(90)

tt.forward(height)

tt.right(90)

tt.forward(height)

tt.right(90)

tt.forward(height)

tt.left(angle1)

tt.forward(triangles)

tt.right(angle2)

tt.forward(triangles)

tt.left(angle1)

tt.forward(height)

tt.right(90)

tt.forward(height)

#Triangle 2
tt.left(angle3)

tt.forward(triangles2)

tt.right(angle4)

tt.forward(triangles2)

tt.left(angle3)

#Triangle 3
tt.forward(height)

tt.right(90)

tt.forward(height)

tt.left(angle1)

tt.forward(triangles)

tt.right(angle2)

tt.forward(triangles)

tt.left(angle1)

tt.forward(height)

tt.right(90)

tt.forward(height)

#Triangle 4
tt.left(angle3)

tt.forward(triangles2)

tt.right(angle4)

tt.forward(triangles2)

##Done
tt.hideturtle()

turtle.done()