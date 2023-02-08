from turtle import Turtle
MOVE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snake_house = []
        self.create_snake()
        self.head = self.snake_house[0]

    def create_snake(self):
        x = -20
        for i in range(0, 3):
            snake = Turtle("square")
            snake.penup()
            snake.color("white")
            snake.goto(x=x, y=0)
            x -= 20
            self.snake_house.append(snake)