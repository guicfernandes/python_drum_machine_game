import pygame
from pygame import mixer


pygame.init()

WIDTH = 1300  # 1400  # 1366
HEIGTH = 700  # 800  # 768

black = (0, 0, 0)
white = (255, 255, 255)
gray = (128, 128, 128)

screen = pygame.display.set_mode([WIDTH, HEIGTH])
pygame.display.set_caption('Beat Maker')
# label_font = pygame.font.Font('freesansbold.ttf', 32)
label_font = pygame.font.Font('Roboto-Bold.ttf', 32)

fps = 60
timer = pygame.time.Clock()


def draw_grid():
    left_box = pygame.draw.rect(screen, gray, [0, 0, 200, HEIGTH-200], 5)
    bottom_box = pygame.draw.rect(screen, gray, [0, HEIGTH-200, WIDTH, 200], 5)


run = True
while(run):
    timer.tick(fps)
    screen.fill(black)
    draw_grid()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
pygame.quit()
