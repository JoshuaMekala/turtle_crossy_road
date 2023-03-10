from turtle import Turtle
FONT = ("Courier", 20, "normal")
POSITION = (-230,260)


class Scoreboard(Turtle):
    
        def __init__(self):
                super().__init__()
                self.penup()
                self.hideturtle()
                self.level = 1
                self.update_scoreboard()

        def update_scoreboard(self):
                self.clear()
                self.goto(POSITION)
                self.write(f"Level: {self.level}", align="center", font=FONT)

        def level_up(self):
                self.level += 1
                self.update_scoreboard()
        
        def game_over(self):
                self.goto(0,0)
                self.write("GAME OVER",align="center",font= FONT)
