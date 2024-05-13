import pygame
import time
import random

# Initialize pygame
pygame.init()

# Set the window size and title
WIDTH, HEIGHT = 400, 200
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rainy Digital Clock")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RAIN_COLORS = [(0, 255, 255), (135, 206, 250), (30, 144, 255)]  # Cyan, Sky Blue, and Dodger Blue

# Load font
font = pygame.font.Font(None, 48)

# Raindrop class
class Raindrop:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(-HEIGHT, 0)
        self.speed = random.randint(5, 15)
        self.color = random.choice(RAIN_COLORS)

    def fall(self):
        self.y += self.speed
        if self.y > HEIGHT:
            self.y = random.randint(-HEIGHT, 0)
            self.x = random.randint(0, WIDTH)

    def draw(self):
        if not (WIDTH // 2 - 70 < self.x < WIDTH // 2 + 90 and HEIGHT // 2 - 70 < self.y < HEIGHT // 2 + 70):
            pygame.draw.line(WINDOW, self.color, (self.x, self.y), (self.x, self.y + 5), 2)

# Function to draw clock
def draw_clock():
    current_time = time.strftime("%I:%M:%S %p")  # 12-hour format with AM/PM
    text = font.render(current_time, True, WHITE)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    WINDOW.blit(text, text_rect)

# Function to draw raindrops
def draw_raindrops(raindrops):
    for drop in raindrops:
        drop.fall()
        drop.draw()

# Main function
def main():
    clock = pygame.time.Clock()
    raindrops = [Raindrop() for _ in range(60)]

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

if __name__ == "__main__":
    main()
