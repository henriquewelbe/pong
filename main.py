import time
from turtle import Screen
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball

BALL_SPEED = 0.060

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('Black')
screen.title('Pong')
screen.tracer(0)

left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))

ball = Ball()

scoreboard = Scoreboard()

screen.listen()
screen.onkey(right_paddle.up, 'Up')
screen.onkey(right_paddle.down, 'Down')
screen.onkey(left_paddle.up, 'w')
screen.onkey(left_paddle.down, 's')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(BALL_SPEED)
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 275 or ball.ycor() < -275:
        ball.bounce_y()
        if BALL_SPEED > 0:
            BALL_SPEED -= 0.001

    # Detect collision with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 310 or ball.distance(left_paddle) < 50 and ball.xcor() < -310:
        ball.bounce_x()
        if BALL_SPEED > 0:
            BALL_SPEED -= 0.001

    # Detect right paddle miss
    if ball.xcor() > 410:
        ball.reset_position()
        scoreboard.l_point()

    # Detect left paddle miss
    if ball.xcor() < -410:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()
