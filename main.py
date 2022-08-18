from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

snake = Snake()
food = Food()
scoreboard = Scoreboard()
user_score = 0
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

game_on = True
screen.update()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset_score()
        snake.reset_snake()

    # Detect collision with its tail.
    for segments in snake.snake_segments[1:]:
        if snake.head.distance(segments) < 10:
            scoreboard.reset_score()
            snake.reset_snake()


screen.exitonclick()
