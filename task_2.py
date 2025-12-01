import turtle


def draw_tree(branch_length: float, angle: float, level: int) -> None:
    """
    Recursively draw a fractal tree using turtle graphics.
    
    This function implements the Pythagoras Tree fractal pattern using branching lines.
    Each branch splits into two smaller branches at the specified angle.
    
    Args:
        branch_length: Length of the current branch
        angle: Branching angle in degrees
        level: Current recursion level (depth)
    """
    if level > 0:
        # Draw the main branch
        turtle.forward(branch_length)

        # Draw the right branch at 45-degree angle (Pythagoras Tree geometry)
        turtle.right(45)
        draw_tree(branch_length * 0.7071, angle, level - 1)  # 0.7071 ≈ 1/√2

        # Return to main branch position and draw left branch
        turtle.left(90)  
        draw_tree(branch_length * 0.7071, angle, level - 1)

        # Return to original position
        turtle.right(45) 
        turtle.backward(branch_length)


def get_user_input() -> int:
    """
    Get recursion level input from the user with validation.
    
    Returns:
        Valid recursion level between 1 and 15
    """
    while True:
        try:
            level = int(input("Enter recursion level (1-15): "))
            if 1 <= level <= 15:
                return level
            else:
                print("Please enter a number between 1 and 15.")
        except ValueError:
            print("Please enter a valid integer.")


def setup_turtle_graphics() -> None:
    """
    Set up the turtle graphics environment for drawing the fractal.
    """
    # Set up the screen
    screen = turtle.Screen()
    screen.bgcolor("white")
    screen.title("Pythagoras Tree Fractal - Turtle Graphics")
    screen.setup(width=800, height=600)
    
    # Set up the turtle
    turtle.left(90)  # Point upward
    turtle.penup()
    turtle.goto(0, -screen.window_height() // 3)  # Start from bottom center
    turtle.pendown()
    turtle.speed(0)  # Fastest drawing speed
    turtle.color("darkred")  
    turtle.pensize(2) 


if __name__ == "__main__":
    # Get user input for recursion level
    level = get_user_input()

    print(f"\nGenerating Pythagoras Tree with recursion level {level}...")
    print("Close the turtle graphics window to exit the program.")

    # Set up turtle graphics
    setup_turtle_graphics()
    
    # Draw the fractal tree
    initial_length = 120
    branching_angle = 45 
    
    draw_tree(initial_length, branching_angle, level)
    
    # Keep the window open
    turtle.done()
