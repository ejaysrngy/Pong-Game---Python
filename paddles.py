from turtle import Turtle, Screen

# 2. Make paddles (have them move up and down); use different coordinates for up and down
#   since the leading head will be either the first or last item on the list

STARTING_POSN = [(-400, 0), (-400, 20), (-400, 40), (-400, 60)]


class PlayerPaddles:
    def __init__(self):
        self.paddle_seg = []
        self.create_paddle()
        self.bottom_seg = self.paddle_seg[0]
        self.top_seg = self.paddle_seg[-1]


    def create_paddle(self):
        for i in STARTING_POSN:
            paddle = Turtle("square")
            paddle.setheading(90)
            paddle.penup()
            paddle.color("white")
            paddle.goto(i)
            self.paddle_seg.append(paddle)

    def follow_top(self):
        new_x, new_y = self.top_seg.xcor(), self.top_seg.ycor()
        for i in self.paddle_seg[-2::-1]:
            new_y -= 20
            i.goto(new_x, new_y)

    def follow_bot(self):
        new_x, new_y = self.bottom_seg.xcor(), self.bottom_seg.ycor()
        for i in self.paddle_seg[1:]:
            new_y += 20
            i.goto(new_x, new_y)

    def move_up(self):
        self.top_seg.forward(10)
        self.follow_top()


    def move_down(self):
        self.bottom_seg.back(10)
        self.follow_bot()


ENEMY_POSITION = [(400, 0),(400, 20),(400, 40),(400, 60)]

class EnemyPaddles:
    def __init__(self):
        self.paddle_seg = []
        self.create_paddle()
        self.bottom_seg = self.paddle_seg[0]
        self.top_seg = self.paddle_seg[-1]

    def create_paddle(self):
        for i in ENEMY_POSITION:
            paddle = Turtle("square")
            paddle.setheading(90)
            paddle.penup()
            paddle.color("white")
            paddle.goto(i)
            self.paddle_seg.append(paddle)

    def moving_up(self):
        self.top_seg.speed(1)
        self.top_seg.forward(10)
        new_x, new_y = self.top_seg.xcor(), self.top_seg.ycor()
        for i in self.paddle_seg[-2::-1]:
            new_y -= 20
            i.goto(new_x, new_y)

    def moving_down(self):
        self.bottom_seg.speed(1)
        self.bottom_seg.back(10)
        new_x, new_y = self.bottom_seg.xcor(), self.bottom_seg.ycor()
        for i in self.paddle_seg[1:]:
            new_y += 20
            i.goto(new_x, new_y)





