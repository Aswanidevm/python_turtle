import turtle
fred = turtle.Turtle()
mary = turtle.Turtle()

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

while True:
    value = fred.xcor()
    fred.forward(1)
    mary.forward(1)
    if value == 100:
       break
print("Reached the limit")






turtle.done()