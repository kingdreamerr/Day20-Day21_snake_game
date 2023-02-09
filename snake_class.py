from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
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
        for position in STARTING_POSITIONS:
            self.add_square(position)
          
    def add_square(self,position):
        snake = Turtle("square")
        snake.penup()
        snake.color("white")
        snake.goto(position)
        self.snake_house.append(snake)

    def extend(self):
        self.add_square(self.snake_house[-1].position())
    def move(self):
        for square in range(len(self.snake_house) - 1, 0, -1):
            new_x = self.snake_house[square - 1].xcor()
            new_y = self.snake_house[square - 1].ycor()
            self.snake_house[square].goto(new_x, new_y)
        self.head.fd(MOVE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)
