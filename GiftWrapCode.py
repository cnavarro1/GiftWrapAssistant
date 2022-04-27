import turtle
import math
from math import *
from turtle import *


try:
    tt = turtle.Turtle()
except:
    tt = turtle.Turtle()
    
ts = turtle.Screen()
run='Y'

while run == 'Y':
    ##tt.clear()
    tt.showturtle()
    realLength = ts.numinput("Dimensions", "Length")
    realWidth = ts.numinput("Dimensions", "Width")
    realHeight = ts.numinput("Dimensions", "Height")
    
    length = realLength*20
    width = realWidth*20
    height = realHeight*20
    
    angle1 = math.degrees(math.atan(length/width))
    angle3 = math.degrees(math.atan((width/length)*1.5))
    angle2 = 180 - (2*math.degrees(math.atan(width/length)))
    angle4 = 180 - (2*math.degrees(math.atan((length/width)*(2/3))))
    
    flap1 = height
    
    triangles = (((width/2)**2)+((length/2)**2))**0.5
    
    triangles2 = (((width*3/4)**2)+((length/2)**2))**0.5
    
    #ts.reset()
    #ts.setworldcoordinates(-120, -180, 420, 270)
    
    tt.speed(5)
    
    #Center drawing
    tt.color('white')
    tt.goto(-length/2, -width/2)
    tt.color('black')
    
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
    tt.right(180-angle3)
    
    ##Done
    tt.hideturtle()
    run = ts.textinput("Restart?", "Enter Y or N")
    ts.listen()
turtle.done()


