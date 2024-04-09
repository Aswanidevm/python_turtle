import turtle
import random

sky = turtle.Screen()
stars = turtle.Turtle()
moon = turtle.Turtle()
sky.setup(1.0, 1.0)
w = round(sky.window_width()/2)
h = round(sky.window_height()/2)
numstars = 200
moonsize = 80

stars.color("white")


moon.color("white")
moon.penup()
moon.setposition(w/2,h/2)
moon.dot(moonsize)
moon.color("black")
# moon.forward(10)
moon.setposition((w/2)-2,(h/2)+5)
moon.dot(moonsize)

sky.bgcolor("black")
sky.tracer(0)


stars.penup()
for i in range (numstars):
    x = random.randint(-w, w)
    y = random.randint(-h, h)
    stars.setposition(x,y)
    stars.dot(random.randint(1,5))
    print(stars.xcor())


sky.update()


turtle.done()