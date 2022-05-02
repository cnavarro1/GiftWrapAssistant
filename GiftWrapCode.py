import turtle
import math

try:
    tt = turtle.Turtle()
except:
    tt = turtle.Turtle()

ts = turtle.Screen()
ts.screensize()
ts.setup(width = 1.0, height = 1.0)

run='Y'
#Check Units
units = ts.textinput("Units", "Inches or Centimers?: I or C")    
while run == 'Y' or run == 'y':
    tt.clear()
    tt.showturtle()
    

    
    
    #Dimension Input
    realLength = ts.numinput("Dimensions", "Length")
    realWidth = ts.numinput("Dimensions", "Width")
    realHeight = ts.numinput("Dimensions", "Height")
    
    if units == 'c' or units == 'C':
        realLength = realLength/2.54
        realWidth = realWidth/2.54
        realHeight = realHeight/2.54
    
    #Convert inches to pixels
    width = realWidth*20
    length = realLength*20
    height = realHeight*20
    
    #Calculate angles needed to turn properly
    angle1 = math.degrees(math.atan(width/length))
    angle3 = math.degrees(math.atan((length/width)*1.5))
    angle2 = 180 - (2*math.degrees(math.atan(length/width)))
    angle4 = 180 - (2*math.degrees(math.atan((width/length)*(2/3))))
    
    angle5 = 90-angle3+angle4
    
    flap1 = height
    
    #Calculate triangle lengths
    triangles = (((length/2)**2)+((width/2)**2))**0.5
    triangles2 = (((length*3/4)**2)+((width/2)**2))**0.5
    
    #Define size variables in x and y
    y = height + (1.25*length)
    x = height + width
    
    #Set Speed
    tt.speed(10)
    
    if x <= 940 and y <= 495:
        ##BEGIN DRAWING
        #Center drawing
        tt.color('white')
        tt.setpos(-width/2, -length/2)
        tt.color('black')
        
        ##Center Box
        tt.forward(width)
        tt.left(90)
        tt.forward(length)
        tt.left(90)
        tt.forward(width)
        tt.left(90)
        tt.forward(length)
        
        ##Height boxes
        tt.color('red')
        tt.forward(height)
        tt.color('black')
        tt.left(90)
        tt.forward(width)
        tt.color('red')
        tt.left(90)
        tt.forward(height)
        tt.color('black')
        tt.right(90)
        tt.forward(height)
        tt.left(90)
        tt.forward(length)
        tt.left(90)
        tt.forward(height)
        tt.right(90)
        tt.color('red')
        tt.forward(height)
        tt.color('black')
        tt.left(90)
        tt.forward(width)
        tt.color('red')
        tt.left(90)
        tt.forward(height)
        tt.color('black')
        tt.right(90)
        tt.forward(height)
        tt.left(90)
        tt.forward(length)
        tt.left(90)
        tt.forward(height)
        
        ##Flaps and Triangles
        tt.color('red')
        
        #Triangle 1
        tt.right(90)
        tt.forward(width/3)
        tt.right(90)
        tt.forward(height)
        tt.right(90)
        tt.forward(width/3)
        tt.left(angle1)
        tt.forward(triangles)
        tt.right(angle2)
        tt.forward(triangles)
        tt.left(angle1)
        tt.forward(width/3)
        tt.right(90)
        tt.forward(height)
        tt.left(90)
        tt.forward(height-(width/3))
        tt.right(90)
        
        #Triangle 2
        tt.left(angle3)
        tt.forward(triangles2)
        tt.right(angle4)
        tt.forward(triangles2)
        tt.left(angle3)
        tt.right(90)
        tt.forward(height-(width/3))
        tt.left(90)
        
        #Triangle 3
        tt.forward(height)
        tt.right(90)
        tt.forward(width/3)
        tt.left(angle1)
        tt.forward(triangles)
        tt.right(angle2)
        tt.forward(triangles)
        tt.left(angle1)
        tt.forward(width/3)
        tt.right(90)
        tt.forward(height)
        tt.left(90)
        tt.forward(height-(width/3))
        tt.right(90)
        
        #Triangle 4
        tt.left(angle3)
        tt.forward(triangles2)
        tt.right(angle4)
        tt.forward(triangles2)
        tt.right(180-angle3)
    elif x <= 1840 and y <= 990:
        ##BEGIN DRAWING
        originx = -x/2
        originy = -y/2
        #Center drawing
        tt.color('white')
        tt.setpos(originx, originy)
        tt.color('black')
        
        ##Center Box
        tt.left(90)
        tt.forward(length/2)
        tt.right(90)
        tt.forward(width/2)
        tt.right(90)
        tt.forward(length/2)
        tt.right(90)
        tt.forward(width/2)
        
        #sides
        tt.up()
        tt.goto(originx, originy+(length/2))
        tt.down()
        tt.right(90)
        tt.forward(height)
        tt.right(90)
        tt.forward(width/2)
        tt.right(90)
        tt.color('red')
        tt.forward(height)
        tt.color('black')
        tt.left(90)
        tt.forward(height)
        tt.right(90)
        tt.forward(length/2)
        tt.right(90)
        tt.forward(height)
        
        #triangles and flaps
        tt.up()
        tt.goto(originx, originy+(length/2)+height)
        tt.down()
        tt.right(90)
        tt.forward(.75*length)
        tt.right(angle5)
        tt.color('red')
        tt.forward(triangles2)
        tt.right(90-angle3)
        tt.forward(height-(width/3))
        tt.left(90)
        tt.forward(height)
        tt.right(90)
        tt.forward(width/3)
        tt.left(angle1)
        tt.forward(triangles)
        tt.color('black')
        tt.right(angle2+90-angle1)
        tt.forward(width/2)
        tt.right(180)
    else:
        tt.write("Dimensions too large, try entering your shortest dimension as height and longest as width", align= "center", font=['Arial', 20, 'bold'])
        
        
    ##Done
    tt.hideturtle()
    run = ts.textinput("Restart?", "Restart?: Y or N")
    ts.listen()
turtle.done()


