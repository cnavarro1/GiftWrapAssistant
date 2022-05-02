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

#Calibration
calibrate = ts.textinput("Calibration", "Recalibrate?: Y or N")      

if calibrate == 'Y' or calibrate == 'y':
    tt.clear()
    tt.showturtle()
    tt.up()
    tt.goto(0,200)
    tt.down()
    tt.write("Measure the line in chosen units and type it in", align= "center", font=['Arial', 10, 'bold'])
    tt.up()
    tt.goto(-50,0)
    tt.down()
    tt.forward(100)
    tt.hideturtle()
    line = ts.numinput("Calibration", "How long is the line?")
    convert = 100/line
   
while run != 'N' and run != 'n':
    
    tt.clear()
    tt.showturtle()
    
    #Dimension Input
    realLength = ts.numinput("Dimensions", "Length")
    realWidth = ts.numinput("Dimensions", "Width")
    realHeight = ts.numinput("Dimensions", "Height")
    
    if units == 'c' or units == 'C':
        centiLength = realLength
        centiWidth = realWidth
        centiHeight = realHeight
        realLength = realLength/2.54
        realWidth = realWidth/2.54
        realHeight = realHeight/2.54
    
    #Convert inches to pixels
    width = realWidth*convert
    length = realLength*convert
    height = realHeight*convert
    
    #Calculate angles needed to turn properly
    angle1 = math.degrees(math.atan(width/length))
    angle3 = math.degrees(math.atan((length/width)*1.5))
    angle2 = 180 - (2*math.degrees(math.atan(length/width)))
    angle4 = 180 - (2*math.degrees(math.atan((width/length)*(2/3))))
    
    angle5 = 90-angle3+angle4
    
    flap = 3*35.5555556
    
    #Calculate triangle lengths
    triangles = (((length/2)**2)+((width/2)**2))**0.5
    triangles2 = (((length*3/4)**2)+((width/2)**2))**0.5
    
    #Define size variables in x and y
    y = height + (1.25*length)
    x = height + width
    
    #Set Speed
    tt.speed(10)
    
    if x <= 764.44 and y <= 416:
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
        tt.forward(height/2)
        tt.right(90)
        tt.forward(height)
        tt.right(90)
        tt.forward(height/2)
        tt.left(angle1)
        tt.forward(triangles)
        tt.right(angle2)
        tt.forward(triangles)
        tt.left(angle1)
        tt.forward(height/2)
        tt.right(90)
        tt.forward(height)
        tt.left(90)
        tt.forward(height-(height/2))
        tt.right(90)
        
        #Triangle 2
        tt.left(angle3)
        tt.forward(triangles2)
        tt.right(angle4)
        tt.forward(triangles2)
        tt.left(angle3)
        tt.right(90)
        tt.forward(height-(height/2))
        tt.left(90)
        
        #Triangle 3
        tt.forward(height)
        tt.right(90)
        tt.forward(height/2)
        tt.left(angle1)
        tt.forward(triangles)
        tt.right(angle2)
        tt.forward(triangles)
        tt.left(angle1)
        tt.forward(height/2)
        tt.right(90)
        tt.forward(height)
        tt.left(90)
        tt.forward(height-(height/2))
        tt.right(90)
        
        #Triangle 4
        tt.left(angle3)
        tt.forward(triangles2)
        tt.right(angle4)
        tt.forward(triangles2)
        tt.right(180-angle3)
        
    elif x <= 1529 and y <= 990:
        
        pieceX = (2*realWidth)+(2*realHeight)
        pieceY = (2.5*realLength)+(2*realHeight)
        
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
        tt.forward(height-(height/2))
        tt.left(90)
        tt.forward(height)
        tt.right(90)
        tt.forward(height/2)
        tt.left(angle1)
        tt.forward(triangles)
        tt.color('black')
        tt.right(angle2+90-angle1)
        tt.forward(width/2)
        tt.right(180)
        
        tt.color('black')
        tt.up()
        tt.goto(0,200)
        tt.down()
        if units == 'c' or units == 'C':
            pieceX = (2*centiWidth)+(2*centiHeight)
            pieceY = (2.5*centiLength)+(2*centiHeight)
            tt.write("Cut out a rectangle that is " + str(pieceX) + " cm by " + str(pieceY) + " cm", align= "center", font=['Arial', 15, 'bold'])
        else:
            pieceX = (2*realWidth)+(2*realHeight)
            pieceY = (2.5*realLength)+(2*realHeight)
            tt.write("Cut out a rectangle that is " + str(pieceX) + " in. by " + str(pieceY) + "in.", align= "center", font=['Arial', 15, 'bold'])
            
    else:
        tt.color('black')
        tt.up()
        tt.goto(0,100)
        tt.down()
        tt.write("Dimensions too large, try entering your shortest dimension as height and longest as width", align= "center", font=['Arial', 20, 'bold'])
        
    ##Donei
    tt.hideturtle()
    run = ts.textinput("Restart?", "Restart Program?: Y or N")
    ts.onkey(turtle.bye, "Escape")
    ts.listen()
    if run == 'n' or run == 'N':
        tt.color('black')
        tt.up()
        tt.goto(0,0)
        tt.down()
        tt.write("press [Esc] button to close", align= "center", font=['Arial', 10, 'bold'])

turtle.done()