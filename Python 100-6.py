# while loop
# while sth_is_true:
# do this
# then do this
# then do this

# infinite loop
# Project_Escaping the Maze

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while front_is_clear():
    move()
turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
