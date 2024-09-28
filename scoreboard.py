from turtle import Turtle

FONT = ("Courier", 14, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.LEVEL = 1
        self.penup()
        self.hideturtle()
        self.goto(-280, 260)

    def update_score(self):
        self.clear()
        self.write(f"Level : {self.LEVEL}", False, "left", FONT)

    def up_level(self):
        self.LEVEL += 1

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("Game Over", False, "center", ("Courier", 24, "normal"))