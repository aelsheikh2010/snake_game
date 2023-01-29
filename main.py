from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

# my solution to create snake
# x_pos = [0, -20, -40]
# for turtle_index in range(3):
#     new_turtle = Turtle(shape="square")
#     new_turtle.color("white")
#     new_turtle.goto(x=x_pos[turtle_index], y=0)

#another solution
starting_position = [(0, 0), (-20, 0), (-40, 0)]
for position in starting_position:
    segment = Turtle(shape="square")
    segment.color("white")
    segment.goto(position)






screen.exitonclick()