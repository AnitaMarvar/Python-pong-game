from turtle import Screen,Turtle
from ball import Ball
from paddle import Paddle
from scoreboard import ScoreBoard
import time
screen = Screen()
screen.bgcolor("Black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)   #animation gets turned off

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))      #kitne bhi paddle bana sakte hai aise classes

ball = Ball()
scoreboard = ScoreBoard()
#creating a paddle
#in paddle.py

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    #detection with wall
    if ball.ycor() > 280 or ball.ycor() < -280 :
        #needs to bounce
        ball.bounce_y()

    #detect with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect is right cordinate misses the ball
    if ball.xcor() > 280:
        ball.reset_position()
        scoreboard.l_point()

    # when left paddle misses
    if ball.xcor() < -280:
        ball.reset_position()
        scoreboard.r_point()
        
screen.exitonclick()