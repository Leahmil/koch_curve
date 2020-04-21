import turtle
import math

def koch_snowflake(length, iterations):
    '''This function generates up to 7 iterations of a koch snowflake fractal.

    Parameters:

        length (int): Length of one side of the initial triangle, to control the overall size of the fractal.

        iterations (int): The total number of loops around the initial triangle.
    '''

    if iterations > 7 or length > 700:
        print("iterations limit set at 7, length limit set at 700")
        return

    # turtle/canvas setup
    turtle.setup(900, 900)
    turtle_xpos = -1 * (length/2)
    turtle_ypos = -2/3 * (((math.sqrt(3)/2)*length)/2)
    turtle.penup()
    turtle.goto(turtle_xpos, turtle_ypos)
    turtle.pendown()
    turtle.speed(0)
    turtle.color('#B0C4DE')


    # intial turtle triangle, not included as an iteration
    turtle.forward(length)
    turtle.left(120)
    turtle.forward(length)
    turtle.left(120)
    turtle.forward(length)

    # list to determine when the turtle should turn right instead of left, see below
    right_angle_list = []


    for n in range(iterations):
        # for each iteration divide the length of each side by 3
        len_side = length / 3
        length = len_side

        # modify the line color each iteration
        colors = ['#87CEFA', '#6495ED', '#00BFFF', '#1E90FF', '#0000FF', '#0000CD', '#00008B', '#191970']
        color = colors[n+1]
        turtle.color(color)

        ### for the right angle list: ###
        # After mapping out a few iterations,
        # I found trends for when the turtle should turn right instead of left
        # (there is probably a more mathematically efficient way of doing this!)

        # get the number of sides per n iteration and the total number of sides for all iterations.
        n_sides = 3 * 4 ** n
        total_sides = int(3 * 4 ** (iterations-1))
        # the n_start tells us when to start and at what interval to turn right instead of left.
        n_start = int(4 ** (n-1))
        interval = math.ceil((4 ** n)/2)

        for num in range(n_start, total_sides, interval):
            if n >= 2:
                right_angle_list.append(num)
        # To check out the right angle list:
        # print("right angle list for iteration {}: {}".format(n+1, right_angle_list))

        for side in range(n_sides):
            # turn right instead of left to get to the right starting point for the next triangle: _/\_
            if n >= 1 and (side % 2 != 0 or side in right_angle_list):
                turtle.right(60)
            else:
                turtle.left(120)

            # set of 4 sides to complete a triangle for each loop _/\_
            turtle.forward(len_side)
            turtle.right(60)
            turtle.forward(len_side)
            turtle.left(120)
            turtle.forward(len_side)
            turtle.right(60)
            turtle.forward(len_side)

koch_snowflake(500, 5)

turtle.done()