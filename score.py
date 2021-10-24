from turtle import Turtle

class PlayerScore(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(-100, 190)
        self.color("white")
        self.score = 0
        self.write(arg=self.score, align="left", font=("Courier", 40))

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(arg=self.score, align="left", font=("Courier", 40))


class EnemyScore(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(75, 190)
        self.color("white")
        self.score = 0
        self.write(arg=self.score, align="left", font=("Courier", 40))

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(arg=self.score, align="left", font=("Courier", 40))