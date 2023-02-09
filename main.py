from turtle import Screen
from snake_class import Snake
from food import Food
from scoreboard import Board
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")


screen.tracer(0)
snake = Snake()
screen.listen()
food = Food()
board = Board()
# game_over_text = Board()

screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down,"Down")
screen.onkeypress(snake.left,"Left")
screen.onkeypress(snake.right,"Right")
score = 0
is_end = False
while not is_end:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # EAT FOOD 
    if snake.head.distance(food) < 15:
        food.refresh()
        score += 1
        snake.extend()
        board.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -295 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        is_end = True
        time.sleep(0)
        board.game_over()

    # Detect collision with the tail.
    for square in snake.snake_house[1:]:
        if snake.head.distance(square) < 10:
            is_end = True
            board.game_over()

screen.exitonclick()
