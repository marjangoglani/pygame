import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()

sky_surface = pygame.Surface((800, 400))
sky_surface.fill('cadetblue1')
wabbit_surface = pygame.image.load('wabbit.png')
ground_surface = pygame.Surface((800, 100))
ground_surface.fill('chartreuse4')


while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface,(0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(wabbit_surface, (0, 200))

    pygame.display.update()
    clock.tick(60)  # this while loop runs at most 60fps
