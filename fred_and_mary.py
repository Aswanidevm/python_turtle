import turtle
fred = turtle.Turtle()
mary = turtle.Turtle()

import random
fspeed = random.randint(1, 23)
mspeed = random.randint(1, 20)
print(fspeed , mspeed)

fred.shape("turtle")
fred.color("blue")
mary.shape("turtle")
mary.color("pink")
mary.left(180)
# def forward_to_both(value):
#     """Forwards a value to both fred and mary functions."""
#     fred.forward(value)
#     mary.forward(value)
#
# i = 0
# while i < 100:
#     forward_to_both(i)  # Call the combined forwarding function
#     i += 1
#
# print("Finished forwarding values.")  # Informative output
target = 159
x=1
y=1
# while True:
#     fvalue = fred.xcor()
#     mvalue = mary.xcor()
#     print(fvalue , mvalue)
#     fred.forward(fspeed)
#     mary.forward(mspeed)
#     if fvalue >= (target) or mvalue <= -(target):
#         break

while  fred.xcor() <= (target) and mary.xcor() >= -(target):
    fvalue = fred.xcor()
    mvalue = mary.xcor()
    print(fvalue , mvalue)
    fred.forward(x)
    mary.forward(y)
    x = x+1
    y = x
    fred.tilt(10)
    mary.tilt(10)
    # fred.left(5)
    # fred.turtlesize(2)
    # if fvalue >= (target) or mvalue <= -(target):
    #     break

print("Reached the limit")

turtle.done()