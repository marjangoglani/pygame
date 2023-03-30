import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()
text_font = pygame.font.Font(None, 50)

sky_surface = pygame.Surface((800, 400))
sky_surface.fill('cadetblue1')

wabbit_surface = pygame.image.load('wabbit.png').convert_alpha()

bad_bush_surface = pygame.image.load('bad_bush.png').convert_alpha()
bad_bush_x_pos = 600

ground_surface = pygame.Surface((800, 100))
ground_surface.fill('chartreuse4')

text_surface = text_font.render("Wabbit Boi", False, "Red")


while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface,(0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(wabbit_surface, (10, 205))
    screen.blit(bad_bush_surface, (bad_bush_x_pos, 260))
    bad_bush_x_pos -= 2
    if (bad_bush_x_pos < -50):
        bad_bush_x_pos = 800
    screen.blit(text_surface, (300, 50))

    pygame.display.update()
    clock.tick(60)  # this while loop runs at most 60fps




# =================== PYGAME TIPS =================== #

''' surface is used for image information while ractangle
    is used for placement '''