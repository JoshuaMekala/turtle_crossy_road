import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move,"Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.gen_car()
    cars.move_cars()

    # detects collision with cars
    for car in cars.all_cars:
        if player.distance(car) < 25:
            game_is_on = False
            scoreboard.game_over()
    
    # checks if we've reached the end and then speeds up the cars:
        if player.won_level():
            cars.speed_up()
            scoreboard.level_up()
    


screen.exitonclick()