import pygame
import random


pygame.init()


WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Night City")


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BROWN = (52, 33, 4)
GRAY = (128, 128, 128)


def draw_stars():
    for _ in range(50):
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT)
        pygame.draw.circle(screen, WHITE, (x, y), 2)


def draw_buildings():
    building_positions = [(50, HEIGHT - 250), (200, HEIGHT - 200), (350, HEIGHT - 300),
                          (450, HEIGHT - 250), (600, HEIGHT - 200), (750, HEIGHT - 300)]
    building_sizes = [(60, 150), (80, 180), (100, 200)]

    for i, (x, y) in enumerate(building_positions):
        building_width, building_height = building_sizes[i % 3] 
        building_bottom = HEIGHT - 100  
        pygame.draw.rect(screen, BROWN, (x, building_bottom - building_height, building_width, building_height)) 
        for window_x in range(x + 5, x + building_width - 5, 20):  
            for window_y in range(building_bottom - building_height + 5, building_bottom - 20, 30):
                if random.random() < 0.7:  
                    pygame.draw.rect(screen, YELLOW, (window_x, window_y, 10, 20))

def draw_moon():
    pygame.draw.circle(screen, WHITE, (100, 100), 80)


def draw_road():
    pygame.draw.rect(screen, GRAY, (0, HEIGHT - 100, WIDTH, 100))
    for i in range(0, WIDTH, 80): 
        pygame.draw.line(screen, WHITE, (i, HEIGHT - 50), (i + 40, HEIGHT - 50), 5)


def draw_sidewalk():
    pygame.draw.rect(screen, BLACK, (0, HEIGHT - 100, WIDTH, 20)) 


running = True
clock = pygame.time.Clock()  
while running:
    screen.fill(BLACK)  
    draw_stars() 
    draw_sidewalk()  
    draw_road()  
    draw_buildings()  
    draw_moon()  


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()  
    clock.tick(1)  


pygame.quit()
