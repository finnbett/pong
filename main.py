from turtle import Turtle, Screen
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong")
screen.bgcolor("black")
screen.tracer(0)
#TODO: Create and move the paddle
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))


screen.listen()
screen.onkey(right_paddle.move_paddle_up, "Up")
screen.onkey(right_paddle.move_paddle_down, "Down")
screen.onkey(left_paddle.move_paddle_up, "w")
screen.onkey(left_paddle.move_paddle_down, "s")

game_is_on = True
while game_is_on:
    screen.update()


screen.exitonclick()
#TODO: CREATE ANOTHER PADDLE
#TODO: CREATE THE BALL AND MAKE IT MOVE
#TODO: DETECT COLLIISON WITH WALL AND BOUNCE
#TODO: DETECT COLLISION WITH THE PADDLE AND BOUNCE
#TODO: DETECT COLLISION WITH WALLS ON X AXIS
#TODO: TRACK THE SCORE.