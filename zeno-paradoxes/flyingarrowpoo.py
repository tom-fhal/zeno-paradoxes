import time
import pygame

pygame.init()

window = pygame.display.set_mode((640, 480))

background = pygame.Surface((640, 480))

background.fill((255, 255, 255))

pygame.display.flip()

# Define the Arrow class
class Arrow:
    # Define the constructor, which initializes the object's attributes
    def __init__(self, position, speed, name):
        self.position = position # The position of the Arrow (in m)
        self.speed = speed # The speed of the Arrow (in m/s)
        self.name = name # The name of the Arrow

    # Define the advance method, which updates the position based on the speed
    def advance(self):
        self.position += self.speed # The new position is equal to the old one plus the product of the speed and the elapsed time (1 s)

# Define the Target class
class Target:
    # Define the constructor, which initializes the object's attributes
    def __init__(self, position, name , speed):
        self.position = position # The position of the Target (in m)
        self.name = name # The name of the Target
        self.speed = speed # The speed of the Target (in m/s)
    #def distance(self):
        #self.position = self.position - self.speed
# Create arrow and target instances
arrow = Arrow(0, 25, "Arrow")
target = Target(200, "Target",25)
def launch2():

    # Initialize elapsed time (in s)
    time_elapsed = 0

    screen = pygame.display.set_mode((800, 600))

    font = pygame.font.SysFont("Arial", 20)
    arrow_image = pygame.image.load('sprites/arrow.png')
    target_image = pygame.image.load('sprites/target.png')

    arrow_image = pygame.transform.scale(arrow_image, (50, 50))
    target_image = pygame.transform.scale(target_image, (50, 50))

    # Create a loop to simulate each step of the race
    while arrow.position < target.position:
        screen.fill((255, 255, 255))

        for event in pygame.event.get():

                # If the user closes the window

                if event.type == pygame.QUIT:
                    # Quit the program

                    pygame.quit()

                    exit()

                # If the user presses the Esc key
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:

                    # Quit the program

                    pygame.quit()
                    exit()

        # Display the positions of the Arrow and Target at each step of the course
        print(f"At T {time_elapsed}: {arrow.name} is {arrow.position} meters from target and {target.name} is {target.position} meters away.")

        # At each iteration, advance the Arrow using its method
        arrow.advance()
        screen.blit(target_image,(int(target.position)*3 - target_image.get_width() // 2 ,200 - target_image.get_height() // 2))
        screen.blit(arrow_image,(int(arrow.position)*3 - arrow_image.get_width() // 2 ,200 - arrow_image.get_height() // 2))
        
        text_surface_arrow = font.render(f"Arrow: {arrow.position}m", True, (0,0,0))
        text_surface_target = font.render(f"Target: {target.position}m", True, (0,0,0))
        
        screen.blit(text_surface_arrow,(int(arrow.position)*3 - text_surface_arrow.get_width() // 2 ,200 + arrow_image.get_height() // 2 + text_surface_arrow.get_height()))
        screen.blit(text_surface_target,(int(target.position)*3 - text_surface_target.get_width() // 2 ,200 + target_image.get_height() // 2 + text_surface_target.get_height()))

        time_elapsed += 1

        pygame.display.flip()

        time.sleep(1.5)

if __name__ == "__main__":
    launch2()
