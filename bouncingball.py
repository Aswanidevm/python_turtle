import random
import turtle
# ball_y_velo = 10
# ball_x_velo = -4
gra = -0.01
energy_retained = 0.9
no_balls = 50

window = turtle.Screen()
window.setup(900 , 700)
balls = []
for p in range(no_balls):
    ball = turtle.Turtle()
    ball.penup()
    ball.setposition(
        random.randint(-100,100),
        random.randint(-100, 100)
    )
    ball.yvelocity = random.randint(-3,3)
    ball.xvelocity = random.randint(-5,5)
    ball.shape("circle")
    ball.color(random.random(), random.random(), random.random())

    balls.append(ball)

# for x in range(200):
#     ball.sety(ball.ycor()-2)
while True:
    for ball in balls:

        # ball.sety(ball.ycor() + ball_y_velo)
        ball.sety(ball.ycor() + ball.yvelocity)
        # ball_y_velo += gra
        ball.yvelocity += gra
        # ball.setx(ball.xcor()+ ball_x_velo)
        ball.setx(ball.xcor()+ ball.xvelocity)
        print(f"ball's position is {ball.ycor():.2f}, the ball's y_velocity is {ball.yvelocity:.2f}")
        if ball.ycor() <= -((window.window_height()/2)-16):
            # ball_y_velo = -ball_y_velo * energy_retained
            ball.yvelocity = -ball.yvelocity * energy_retained
            ball.sety((window.window_height()/2)-16)
        if abs(ball.xcor()) >= ((window.window_width()/2)-16):
            ball.xvelocity = -ball.xvelocity

turtle.done()