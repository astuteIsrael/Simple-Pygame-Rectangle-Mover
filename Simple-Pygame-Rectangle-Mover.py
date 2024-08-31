import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Simple Pygame Example")

# Set up the rectangle (player)
rect_color = (0, 128, 255)
rect_width, rect_height = 60, 60
rect_x, rect_y = (screen_width - rect_width) // 2, (screen_height - rect_height) // 2
rect_speed = 5

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the rectangle using arrow keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        rect_x -= rect_speed
    if keys[pygame.K_RIGHT]:
        rect_x += rect_speed
    if keys[pygame.K_UP]:
        rect_y -= rect_speed
    if keys[pygame.K_DOWN]:
        rect_y += rect_speed

    # Ensure the rectangle stays within the screen boundaries
    rect_x = max(0, min(rect_x, screen_width - rect_width))
    rect_y = max(0, min(rect_y, screen_height - rect_height))

    # Fill the screen with white
    screen.fill((255, 255, 255))

    # Draw the rectangle
    pygame.draw.rect(screen, rect_color, (rect_x, rect_y, rect_width, rect_height))

    # Update the display
    pygame.display.flip()

    # Frame rate
    pygame.time.Clock().tick(60)
