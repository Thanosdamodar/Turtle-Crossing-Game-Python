import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.tracer(0)
car_manager = CarManager()
player = Player()
scoreboard = Scoreboard()
screen.setup(width=600, height=600)

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    scoreboard.update_score()
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.move_cars()


    if player.ycor() > 280:
        scoreboard.up_level()
        car_manager.speed_up()
        player.restore_player()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False


screen.exitonclick()
