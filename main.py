from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong")
screen.bgcolor("black")
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
score = Score()


screen.listen()
screen.onkey(right_paddle.move_paddle_up, "Up")
screen.onkey(right_paddle.move_paddle_down, "Down")
screen.onkey(left_paddle.move_paddle_up, "w")
screen.onkey(left_paddle.move_paddle_down, "s")

game_is_on = True
while game_is_on:
    game_speed = ball.game_speed
    time.sleep(game_speed)
    screen.update()
    ball.ball_move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()


    #detect collision with the right paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) <50 and ball.xcor() < -320:
        ball.bounce_x()


    #detecct if ball is out of bounds
    if ball.xcor() > 380:
        ball.reset()
        score.left_point()
        score.update_score()

    if ball.xcor() < -380:
        ball.reset()
        score.right_point()
        score.update_score()







screen.exitonclick()

#TODO: CREATE THE BALL AND MAKE IT MOVE
#TODO: DETECT COLLIISON WITH WALL AND BOUNCE
#TODO: DETECT COLLISION WITH THE PADDLE AND BOUNCE
#TODO: DETECT COLLISION WITH WALLS ON X AXIS
#TODO: TRACK THE SCORE.