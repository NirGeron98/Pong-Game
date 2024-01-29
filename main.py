from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
scoreboard = Scoreboard()
screen.bgcolor("black")
screen.setup(width=800, height= 600)
screen.title("Pong")

right_paddle = Paddle((350,0), screen=screen, up_key="Up",down_key="Down")
left_paddle = Paddle((-350, 0), screen=screen, up_key="w",down_key="s")
ball = Ball()

screen.listen()


is_game_on = True
while is_game_on:
    time.sleep(0.05)
    screen.update()
    ball.move()

    #Detect collision
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    #Detect collision with right paddle:
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()
    #Detect collision with left paddle:
    if ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    
    #Detect when paddle misses ball:
    if ball.xcor() >= 380: 
        ball.reset_position()

        scoreboard.l_point()
    
    if ball.xcor() <=-380:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()