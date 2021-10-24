# TODO 1. Make main screen
from turtle import Turtle, Screen
from paddles import PlayerPaddles, EnemyPaddles
from ball import Ball
from score import PlayerScore, EnemyScore

import time
import random as r

# 4. have the ball move around the screen
# 5. have the ball interact with the paddles
# 6. if ball moves out of bounds, score the player
# 7. keep track of score


# TODO 1. main screen
screen = Screen()
screen.bgcolor("black")
screen.tracer(0)
screen.setup(height=500, width=900)
# 1.1 dashed line in the middle
line = Turtle()
line.goto(0, 350)
line.penup()
line.right(90)
line.hideturtle()
line.pensize(8)
line.pencolor("white")
for i in range(20):
    line.pendown()
    line.forward(10)
    line.penup()
    line.forward(30)

# 2. Make paddles (have them move up and down)
paddle = PlayerPaddles()
enemy = EnemyPaddles()

screen.onkeypress(paddle.move_down, "s")
screen.onkeypress(paddle.move_up, "w")

# 3. Make enemy paddles(moving up and down)
screen.onkeypress(enemy.moving_up, "Up")
screen.onkeypress(enemy.moving_down, "Down")
screen.listen()

# 3. Make the ball
ball = Ball()

# 4. make score
p_score = PlayerScore()
e_score = EnemyScore()
sleep_time = 0.100
while True:
    time.sleep(sleep_time)
    screen.update()
    ball.move()

    for i in paddle.paddle_seg:
        if ball.ball.distance(i) < 30:
            ball.paddle_bounce()

    for i in enemy.paddle_seg:
        if ball.ball.distance(i) < 30:
            ball.paddle_bounce()

    if ball.ball.ycor() > 230 or ball.ball.ycor() < -220:
        ball.bounce()

    if ball.ball.xcor() > 460 or ball.ball.xcor() < -460:
        ball.ball.goto(0, 0)

    if ball.ball.xcor() > 450:
        p_score.increase_score()
    elif ball.ball.xcor() < -450:
        e_score.increase_score()

    if (p_score.score + e_score.score) >= 4:
        sleep_time = 0.070
        if (p_score.score + e_score.score) >= 8:
            sleep_time = 0.025
