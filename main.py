import turtle
from turtle import Screen
from snake import Snake
from food import Food
from score import Scoreboard
import time

# Create the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game by Namrata")
screen.tracer(0)

# Create objects
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Control the snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Game loop flag
game_is_on = True

try:
    while game_is_on:
        screen.update()
        time.sleep(0.5)
        snake.move()

        # Detect collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()
            # Detect collision with food
        if snake.head.xcor()>280 or snake.head.xcor() < -280 or snake.head.ycor()> 280 or snake.head.ycor() < -280:
            game_is_on=False
            scoreboard.game_over()

        #detect collision with tail
        for segment in snake.segments:
            if segment == snake.head:
                pass
            elif snake.head.distance(segment)  < 10:
                game_is_on =False
                scoreboard.game_over()


except turtle.Terminator:
    print("Game exited cleanly.")

# Exit on click (optional)
screen.exitonclick()
