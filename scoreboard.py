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
    
  def display(self):
    self.write(f"Score: {self.score}", False, align="center",font=('Arial', 15, 'normal'))

  def increase_score(self):
    self.clear()
    self.score +=1
    self.display()