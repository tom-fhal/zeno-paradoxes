import time

import pygame

#def launch_game():

# Define the Achilles class
class Achilles:
    # Define the constructor, which initializes the object's attributes
    def __init__(self, speed, position, name):
        self.speed = speed # The speed of Achilles (in m/s)
        self.position = position # The position of Achilles (in m)
        self.name = name # The name of Achilles

    # Define the advance method, which updates the position based on the speed
    def advance(self, delta_t):
        self.position += self.speed * delta_t # The new position is equal to the old one plus the product of the speed and the elapsed time

# Define the Turtle class
class Turtle:
    # Define the constructor, which initializes the object's attributes
    def __init__(self, speed, position, name):
        self.speed = speed # The speed of the Turtle (in m/s)
        self.position = position # The position of the Turtle (in m)
        self.name = name # The name of the Turtle

    # Define the advance method, which updates the position based on the speed
    def advance(self, delta_t):
        self.position += self.speed * delta_t # The new position is equal to the old one plus the product of the speed and the elapsed time

# Create achilles and turtle instances
achilles = Achilles(10, 0, "Achilles")
turtle = Turtle(5, 50, "Turtle")
def launch():
    # Initialize elapsed time (in s)
    time_elapsed = 0


    screen = pygame.display.set_mode((800, 600))

    pygame.font.init()

    font = pygame.font.SysFont("Arial", 20)

    # Define scale and margin

    scale = 5

    margin = 50

    # Initialize iteration counter

    iterations = 0


    while iterations < 11:

        # Change background color to white

        screen.fill((255, 255, 255))

        for event in pygame.event.get():

            # If user closes window

            if event.type == pygame.QUIT:
                # Quit program

                pygame.quit()

                exit()

            # If user presses Esc key
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:

                # Quit program

                pygame.quit()
                exit()

        # Display positions of Achilles and Turtle at each step of course
        print(f"Time: {time_elapsed} seconds: {achilles.name} is at {achilles.position} meters and {turtle.name} is at {turtle.position} meters.")

        # Calculate time required for Achilles to reach current position of Turtle
        delta_t = (turtle.position - achilles.position) / achilles.speed

        # At each iteration, advance Achilles and Turtle using their respective methods
        achilles.advance(delta_t)
        
        turtle.advance(delta_t)
        time_elapsed += delta_t

        # Draw a red line for Achilles
        pygame.draw.line(screen, (255, 0, 0), (margin, 400), (margin + achilles.position * scale, 400), 5)
        # Draw a green line for Turtle
        pygame.draw.line(screen, (0, 255, 0), (margin, 500), (margin + turtle.position * scale, 500), 5)

                # Create text surfaces for positions of Achilles and Turtle
        achilles_text = font.render(f"{achilles.position} meters", True, (0, 0, 0))
        turtle_text = font.render(f"{turtle.position} meters", True, (0, 0, 0))

        # Create text surfaces for names of Achilles and Turtle
        achilles_name_text = font.render(f"{achilles.name}", True, (0, 0, 0))
        turtle_name_text = font.render(f"{turtle.name}", True, (0, 0, 0))

        # Draw text surfaces next to lines
        screen.blit(achilles_name_text,(45, 420))
        screen.blit(turtle_name_text,(45, 520))

        # Draw text surfaces next to lines
        screen.blit(achilles_text,(margin + achilles.position * scale + 10 ,400 - achilles_text.get_height() // 2))
        screen.blit(turtle_text,(margin + turtle.position * scale + 10 ,500 - turtle_text.get_height() // 2))

        iterations += 1

        pygame.display.flip()

        time.sleep(1.5)

if __name__ == "__main__":
    launch()
