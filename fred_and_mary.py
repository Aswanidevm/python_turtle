import turtle
fred = turtle.Turtle()
mary = turtle.Turtle()

import random
fspeed = random.randint(1, 10)
mspeed = random.randint(1, 10)
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
target = 120
while True:
    fvalue = fred.xcor()
    mvalue = mary.xcor()
    fred.forward(fspeed)
    mary.forward(mspeed)
    if fvalue == (target) or mvalue == -(target):
        break


print("Reached the limit")






turtle.done()