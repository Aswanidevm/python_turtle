import turtle
import random
# turtle_name= ["mary" , "fred", "any", "amy", "vicy"]
# colors= ["red", "yellow", "pink", "green", "grey"]
# turtles=[]
# for x in (turtle_name):
#     x = turtle.Turtle()
#     x.shape("turtle")
#     c=random.choice(colors)
#     x.color(c)
#     d=random.randint(20,50)
#     x.forward(d)
#
#     turtles.append(x)

window = turtle.Screen()
window.tracer(0)

many_turles = []
noft = random.randint(9,50)
for x in range (noft):
    print(x)
    fred = turtle.Turtle()
    fred.shape("turtle")
    fred.penup()
    fred.color(random.random(), random.random(), random.random())
    fred.left(360/noft * x)
    many_turles.append(fred)
#
# for x in range (noft):
#     many_turles[x].forward(100)

while True:
    for a_tur in many_turles:
        a_tur.forward(random.randint(2,5))
        a_tur.tilt(10)
        a_tur.radians()
        if abs(a_tur.xcor()) > window.window_width()/2:
        # if a_tur.xcor() > window.window_width()/2 or a_tur.xcor() < -window.window_width()/2:
            a_tur.setheading(180 - a_tur.heading())
        if a_tur.ycor() > window.window_height()/2 or a_tur.ycor() < -window.window_height()/2:
            a_tur.setheading(- a_tur.heading())

    window.update()

turtle.done()


# many_turtles = []

# many_turtles.append(turtle.Turtle())
# many_turtles.append(turtle.Turtle())
# many_turtles.append(turtle.Turtle())
# many_turtles.append(turtle.Turtle())
# many_turtles.append(turtle.Turtle())
#
# many_turtles[0].forward(56)
# many_turtles[1].left(56)
# many_turtles[2].setposition(25,35)
# many_turtles[3].setposition(56,35)


turtle.done()
