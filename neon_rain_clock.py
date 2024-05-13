import pygame
import time
import random

# Initialize pygame
pygame.init()

# Set the window size and title
WIDTH, HEIGHT = 400, 200
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Neon Rainy Digital Clock")

# Define colors
BLACK = (0, 0, 0)
SKY_BLUE = (135, 206, 250)

# Load font
font = pygame.font.Font(None, 48)

# Function to generate neon colors
def generate_neon_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

# Function to draw clock
def draw_clock():
    current_time = time.strftime("%I:%M:%S %p")  # 12-hour format with AM/PM
    time_parts = current_time[:-3].split(":")  # Exclude AM/PM and split into hours, minutes, seconds
    am_pm = current_time[-2:]

    x = WIDTH // 2 - 70
    y = HEIGHT // 2

    neon_colors = [generate_neon_color() for _ in range(3)]

    for i in range(3):
        color = neon_colors[i]
        text = font.render(time_parts[i], True, color)
        text_rect = text.get_rect(center=(x + i * 60, y))
        WINDOW.blit(text, text_rect)

    text = font.render(" " + am_pm, True, SKY_BLUE)
    text_rect = text.get_rect(center=(x + 200, y))
    WINDOW.blit(text, text_rect)

# Function to draw raindrops
def draw_raindrops(raindrops):
    for drop in raindrops:
        drop.fall()
        drop.draw()

# Main function
def main():
    clock = pygame.time.Clock()
    raindrops = [Raindrop() for _ in range(100)]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the background
        WINDOW.fill(BLACK)

        # Draw raindrops
        draw_raindrops(raindrops)

        # Draw clock
        draw_clock()

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(30)

    pygame.quit()

# Raindrop class
class Raindrop:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(-HEIGHT, 0)
        self.speed = random.randint(5, 15)

    def fall(self):
        self.y += self.speed
        if self.y > HEIGHT:
            self.y = random.randint(-HEIGHT, 0)
            self.x = random.randint(0, WIDTH)

    def draw(self):
        pygame.draw.line(WINDOW, SKY_BLUE, (self.x, self.y), (self.x, self.y + 5), 2)

if __name__ == "__main__":
    main()
