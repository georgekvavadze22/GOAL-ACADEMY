from turtle import *
width(9)
speed(30)
color("orange")
forward(200)
left(90)

forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
#end of square

#drawing a door
forward(70)
color("red")

left(90)


forward(135) 

#height of the door


right(90)
forward(60)
right(90)
forward(135)

color("black")
right(90)
forward(60)
color("orange")
forward(70)
color("black")
penup()
goto(200,200)
pendown()
begin_fill()

forward(200)
right(130)
forward(150)
right(97)
forward(150)
end_fill()

penup()
goto(20,100)
pendown()


color("green")
begin_fill()
width(3)


left(50)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
end_fill()

penup()

goto(185,105)
pendown()
begin_fill()
left(180)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
end_fill()

























exitonclick()
