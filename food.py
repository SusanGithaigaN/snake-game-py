from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        # stretch turtle along it's length & width
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        # move food to random location
        random_x = random.randint(-280, -280)
        random_y = random.randint(-280, -280)
        self.goto(random_x, random_y)