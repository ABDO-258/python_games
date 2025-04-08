import pygame
from os.path import join
import random

#general setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode( (WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('space shooter')
running = True
clock = pygame.time.Clock()


# plain surface
surf = pygame.Surface((100,200))
surf.fill('orange')
x = 100

# importing an image
pathimg = join('images', 'player.png')
print(pathimg)
player_surf = pygame.image.load(pathimg).convert_alpha()
player_rect = player_surf.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
# player_direction = 1
player_direction = pygame.math.Vector2(20, -10)
player_speed = 10

starimgpath = join('images', 'star.png')
star_surf = pygame.image.load(starimgpath).convert_alpha()
star_position = [(random.randint(0,WINDOW_WIDTH), random.randint(0,WINDOW_HEIGHT)) for i in range(20)]

meteor_surf = pygame.image.load(join ('images', 'meteor.png')).convert_alpha()
meteor_rect = meteor_surf.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

laser_surf = pygame.image.load(join ('images', 'laser.png')).convert_alpha()
laser_rect = laser_surf.get_frect(bottomleft = (WINDOW_WIDTH - 20, WINDOW_HEIGHT - 20))
while running:
    clock.tick(24)
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # draw game
    #
    display_surface.fill(color='darkgray')
    for pos in star_position:
        display_surface.blit(star_surf, pos)
   
    display_surface.blit(meteor_surf, meteor_rect)
    display_surface.blit(laser_surf, laser_rect)

    # player movement
    player_rect.center += player_direction



    # player_rect.x += player_direction * 0.4
    # if player_rect.right > WINDOW_WIDTH or player_rect.left < 0:
    #     player_direction *= -1

    # if player_rect.right < WINDOW_WIDTH:
    #     player_rect.left += 0.2
    display_surface.blit(player_surf, player_rect)
    
    pygame.display.flip()

pygame.quit()