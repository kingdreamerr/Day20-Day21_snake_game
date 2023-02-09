from turtle import Turtle

class Board(Turtle):
  def __init__(self):
    super().__init__()
    self.score = 0
    self.color("white")
    self.hideturtle()
    self.penup()
    self.goto(x=0,y=275)
    self.display()
  