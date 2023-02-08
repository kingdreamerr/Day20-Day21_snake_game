from turtle import Screen
from snake_class import Snake
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")


screen.tracer(0)
snake = Snake()
screen.listen()

screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down,"Down")
screen.onkeypress(snake.left,"Left")
screen.onkeypress(snake.right,"Right")

is_end = False
while not is_end:
    screen.update()
    time.sleep(0.1)
    snake.move()


screen.exitonclick()