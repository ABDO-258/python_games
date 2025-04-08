import pygame
from os.path import join
import random

#general setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode( (WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('space shooter')
running = True


# plain surface
surf = pygame.Surface((100,200))
surf.fill('orange')
x = 100

# importing an image
pathimg = join('images', 'player.png')
print(pathimg)
player_surf = pygame.image.load(pathimg).convert_alpha()
starimgpath = join('images', 'star.png')

star_surf = pygame.image.load(starimgpath).convert_alpha()
star_position = [(random.randint(0,WINDOW_WIDTH), random.randint(0,WINDOW_HEIGHT)) for i in range(20)]

while running:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # draw game
    #
    display_surface.fill(color='darkgray')
    for pos in star_position:
        display_surface.blit(star_surf, pos)
    x += 0.1
    display_surface.blit(player_surf, (x,150))
    pygame.display.flip()

pygame.quit()