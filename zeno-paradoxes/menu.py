from zenontortoisepoo import *
from rocktreepoo import *
import pygame
from flyingarrowpoo import *
# Initialize pygame
pygame.init()

# Create a window of 800x600 pixels
window = pygame.display.set_mode((800, 600))

# Give the window a title
pygame.display.set_caption("Zenon's paradoxes")

# Create a surface for the background
background = pygame.Surface((800, 600))

# Fill the background with blue color
background.fill((0, 0, 255)) # Blue

# Load a font
font = pygame.font.SysFont("arial", 32)

# Create text for menu title # Added
title_text = font.render("Zenon's paradoxes", True, (255, 255, 255)) # Added

# Create a rectangle for the menu title # Added
title_rect = title_text.get_rect() # Added
title_rect.center = (400, 100) # Added

# Create texts for game choices
achilles_text = font.render("Achilles and the turtle", True, (255, 255, 255))
dichotomy_text = font.render("Dichotomy paradox", True, (255, 255, 255))
arrow_text = font.render("Flying arrow", True, (255, 255, 255))

# Create rectangles for buttons
achilles_button = achilles_text.get_rect()
achilles_button.center = (400, 250) # Changed
dichotomy_button = dichotomy_text.get_rect()
dichotomy_button.center = (400, 350) # Changed
arrow_button = arrow_text.get_rect()
arrow_button.center = (400, 450) # Changed



# Create a variable for the main loop
continue_game = True

# Main loop
while continue_game:
    # Handle keyboard and mouse events
    for event in pygame.event.get():
        # If user clicks on close button, quit game
        if event.type == pygame.QUIT:
            continue_game = False
        
        # If user clicks with mouse, check if it's on a button
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Get mouse position
            x, y = event.pos
            
            # Check if mouse is on Achilles and turtle button
            if achilles_button.collidepoint(x, y):
                # Launch Achilles and turtle game
                print("Launching Achilles and turtle game")
                launch()
            # Check if mouse is on Dichotomy paradox button
            if dichotomy_button.collidepoint(x, y):
                # Launch Dichotomy paradox game
                print("Launching Dichotomy paradox game")
                launch3()
            # Check if mouse is on Flying arrow button
            if arrow_button.collidepoint(x, y):
                # Launch Flying arrow game
                print("Launching Flying arrow game")
                launch2()
    # Display background on window
    window.blit(background, (0, 0))
    
    # Display menu title text # Added
    window.blit(title_text, title_rect) # Added
    
    # Display texts on buttons
    window.blit(achilles_text, achilles_button)
    window.blit(dichotomy_text, dichotomy_button)
    window.blit(arrow_text, arrow_button)
    
    # Update window display
    pygame.display.flip()
