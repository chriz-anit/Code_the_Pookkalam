import turtle

#create work screen
ws = turtle.Screen()

#define turtle instance
t = turtle.Turtle()

t.speed(speed='fastest')

t.hideturtle()

#Outer most layer
t.pencolor('#004d00')
for i in range(37):
    for j in range(2):
      t.forward(250)
      t.right(90)
      
    t.fillcolor('#ffff00')
    t.begin_fill()
    t.circle(5)
    t.end_fill()
    
    t.fillcolor('#004d00')
    t.begin_fill()
    for j in range(2):
      t.forward(250)
      t.right(90)
    t.left(10)
    t.end_fill()

#Square layer-1
t.pencolor('#e60000')
for i in range(37):
    
    t.fillcolor('#e60000')
    t.begin_fill()
    for j in range(4):
      t.forward(225)
      t.right(90)
    t.left(10)
    t.end_fill()

#Square layer-2
t.left(5)
t.pencolor('#ff3300')
for i in range(37):
    
    t.fillcolor('#ff3300')
    t.begin_fill()
    for j in range(4):
      t.forward(207.5)
      t.right(90)
    t.left(10)
    t.end_fill()

#Square layer-3
t.left(5)
t.pencolor('#ffff00')
for i in range(37):
    
    t.fillcolor('#ffff00')
    t.begin_fill()
    for j in range(4):
      t.forward(193.25)
      t.right(90)
    t.left(10)
    t.end_fill()

#Square layer-4
t.left(5)
t.pencolor('#ffffff')
for i in range(37):
    
    t.fillcolor('#ffffff')
    t.begin_fill()
    for j in range(4):
      t.forward(186.125)
      t.right(90)
    t.left(10)
    t.end_fill()

#Single circle
t.goto(0,0)
t.setheading(0)
t.penup()
t.left(180)
t.forward(240)
t.left(90)
t.pendown()

t.pencolor('#FFD601')
t.fillcolor('#FFD601')
t.begin_fill()
t.circle(240)
t.end_fill()

t.penup()
t.goto(0,0)
t.setheading(0)
t.pendown()

#Hexagon layer-0
t.pencolor('green')
for j in range(6):
    t.fillcolor('green')
    t.begin_fill()
    for i in range(6):
        t.forward(120)
        t.left(300)
    t.end_fill()
    t.left(60)

t.left(30)
for j in range(6):
    t.fillcolor('green')
    t.begin_fill()
    for i in range(6):
        t.forward(120)
        t.left(300)
    t.end_fill()
    t.left(60)

#Circle swirl 
t.pencolor('black')
for i in range(35):
    t.fillcolor('#ffff00')
    t.begin_fill()
    t.circle(100)
    t.right(10)
    t.end_fill()

for i in range(35):
    t.circle(100)
    t.right(10)

#Hexagon-1
t.pencolor('#e60000')
for j in range(6):
    t.fillcolor('#e60000')
    t.begin_fill()
    for i in range(6):
        t.forward(65)
        t.left(300)
    t.end_fill()
    t.left(60)

t.left(30)

t.pencolor('#e60000')
for j in range(6):
    t.fillcolor('#e60000')
    t.begin_fill()
    for i in range(6):
        t.forward(65)
        t.left(300)
    t.end_fill()
    t.left(60)

t.left(15)

#Hexagon-2
t.pencolor('#ff0000')
for j in range(6):
    t.fillcolor('#ff0000')
    t.begin_fill()
    for i in range(6):
        t.forward(60)
        t.left(300)
    t.end_fill()
    t.left(60)

t.left(30)

t.pencolor('#ff0000')
for j in range(6):
    t.fillcolor('#ff0000')
    t.begin_fill()
    for i in range(6):
        t.forward(60)
        t.left(300)
    t.end_fill()
    t.left(60)

t.left(15)

#Hexagon-3
t.pencolor('#ff6600')
for j in range(6):
    t.fillcolor('#ff6600')
    t.begin_fill()
    for i in range(6):
        t.forward(50)
        t.left(300)
    t.end_fill()
    t.left(60)

t.left(30)

t.pencolor('#ff6600')
for j in range(6):
    t.fillcolor('#ff6600')
    t.begin_fill()
    for i in range(6):
        t.forward(50)
        t.left(300)
    t.end_fill()
    t.left(60)

#Inner star-0
t.penup()
t.goto(0,0)
t.setheading(0)
t.left(90)
t.forward(30)
t.left(90)
t.forward(90)
t.left(180)
t.pendown()

t.fillcolor('#ffffff')
t.begin_fill()
t.pencolor('white')
for i in range(5):
  t.forward(180)
  t.right(144)
t.end_fill()


#Inner star-1
t.penup()
t.goto(0,0)
t.setheading(0)
t.left(36)
t.left(90)
t.forward(30)
t.left(90)
t.forward(90)
t.left(180)
t.pendown()

t.fillcolor('#ffffff')
t.begin_fill()
t.pencolor('white')
for i in range(5):
  t.forward(180)
  t.right(144)
t.end_fill()

#Inner circle-2
t.penup()
t.goto(0,0)
t.setheading(0)
t.left(180)
t.forward(45)
t.left(90)
t.pendown()

t.pencolor('#004d00')
t.fillcolor('#004d00')
t.begin_fill()
t.circle(45)
t.end_fill()

t.penup()
t.goto(0,0)
t.setheading(0)
t.pendown()

#Inner circle-1
t.goto(0,0)
t.setheading(0)
t.penup()
t.left(180)
t.forward(35)
t.left(90)
t.pendown()

t.pencolor('#ffff00')
t.fillcolor('#ffff00')
t.begin_fill()
t.circle(35)
t.end_fill()

t.penup()
t.goto(0,0)
t.setheading(0)
t.pendown()

t.pencolor('#e60000')
for j in range(6):
    t.fillcolor('#e60000')
    t.begin_fill()
    for i in range(6):
        t.forward(10)
        t.left(300)
    t.end_fill()
    t.left(60)

t.left(30)

t.pencolor('#e60000')
for j in range(6):
    t.fillcolor('#e60000')
    t.begin_fill()
    for i in range(6):
        t.forward(10)
        t.left(300)
    t.end_fill()
    t.left(60)

#Inner circle-0
t.goto(0,0)
t.setheading(0)
t.penup()
t.left(180)
t.forward(10)
t.left(90)
t.pendown()

t.pencolor('#ffffff')
t.fillcolor('#ffffff')
t.begin_fill()
t.circle(10)
t.end_fill()
