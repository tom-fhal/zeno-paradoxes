import time
import pygame

class Tree:
    def __init__(self, position):
        self.position = position

class Stone:
    def __init__(self, distance, speed):
        self.distance = distance
        self.speed = speed

def launch3():
    pygame.init()

    screen = pygame.display.set_mode((800, 600))
    font = pygame.font.SysFont("Arial", 20)

    stone_image = pygame.image.load('sprites/stone.png')
    tree_image = pygame.image.load('sprites/tree.png')

    stone_image = pygame.transform.scale(stone_image, (30, 30))
    tree_image = pygame.transform.scale(tree_image, (100, 150))

    tree = Tree(10)
    stone = Stone(0, 1)

    for step in range(11):
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
        stone.distance += (tree.position - stone.distance) / 2

        print(f"Step {step}: The rock is from {tree.position - stone.distance} meters to the tree.") 
        #stone.distance += (tree.position - stone.distance) / 2

        screen.blit(tree_image, (tree.position + 600, 200))
        screen.blit(stone_image, (stone.distance * 61, 250))

        stone_text_surface = font.render(f"Stone: {stone.distance}m", True, (0,0,0))
        tree_text_surface = font.render(f"Tree: {tree.position}m", True, (0,0,0))
        
        screen.blit(stone_text_surface,(int(stone.distance)*70 - stone_text_surface.get_width() // 2 ,250 + stone_image.get_height() // 2 + stone_text_surface.get_height()))
        screen.blit(tree_text_surface,(tree.position + 600, 390))
        pygame.display.flip()

        time.sleep(1.5)

# Using classes
if __name__ == "__main__":
    launch3()
