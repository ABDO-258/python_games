import pygame
from os.path import join
import random



class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load(join('images', 'player.png')).convert_alpha()
        self.rect = self.image.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
        self.direction =  pygame.Vector2()
        self.speed = 300

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
        self.direction.normalize() if self.direction else self.direction
        self.rect.center += self.direction * self.speed * dt

        recent_kyes = pygame.key. get_just_pressed()
        if recent_kyes[pygame.K_SPACE]:
            print('fire laser')

class Star(pygame.sprite.Sprite):
    def __init__(self, groups, surf):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(center = (random.randint(0,WINDOW_WIDTH), random.randint(0,WINDOW_HEIGHT)))


#general setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode( (WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('space shooter')
running = True
clock = pygame.time.Clock()


# plain surface
# surf = pygame.Surface((100,200))
# surf.fill('orange')
# x = 100

allsprites = pygame.sprite.Group()
star_surf = pygame.image.load(join('images', 'star.png')).convert_alpha()
for i in range(20):
    Star(allsprites, star_surf)
player = Player(allsprites)


# importing an image
# pathimg = join('images', 'player.png')
# print(pathimg)
# player_surf = pygame.image.load(pathimg).convert_alpha()
# player_rect = player_surf.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
# # player_direction = 1
# player_direction = pygame.math.Vector2()
# player_speed = 300

# starimgpath = join('images', 'star.png')
# star_surf = pygame.image.load(starimgpath).convert_alpha()
# star_position = [(random.randint(0,WINDOW_WIDTH), random.randint(0,WINDOW_HEIGHT)) for i in range(20)]

meteor_surf = pygame.image.load(join ('images', 'meteor.png')).convert_alpha()
meteor_rect = meteor_surf.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

laser_surf = pygame.image.load(join ('images', 'laser.png')).convert_alpha()
laser_rect = laser_surf.get_frect(bottomleft = (WINDOW_WIDTH - 20, WINDOW_HEIGHT - 20))
while running:
    dt = clock.tick() / 1000 # deltatime is in ms divide by 1000 to change to s

    # print(clock.get_fps())

    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
        #     print('the key 1 is pressed')
        # if event.type == pygame.MOUSEMOTION:
        #     print (event.pos)
    allsprites.update(dt)  
    # input 
    # keys = pygame.key.get_pressed()
    # player_direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
    # player_direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
    # player_direction.normalize() if player_direction else player_direction
    # player_rect.center += player_direction * player_speed * dt


    # draw game
    #
    display_surface.fill(color='darkgray')
    
   
    # display_surface.blit(meteor_surf, meteor_rect)
    # display_surface.blit(laser_surf, laser_rect)

    # player movement`
    # if player_rect.bottom > WINDOW_HEIGHT or player_rect.top < 0:
    #     player_direction.y *= -1
    # if player_rect.right > WINDOW_WIDTH or player_rect.left < 0:
    #     player_direction.x *= -1
    # player_rect.center += player_direction * player_speed * dt



    # player_rect.x += player_direction * 0.4
    # if player_rect.right > WINDOW_WIDTH or player_rect.left < 0:
    #     player_direction *= -1

    # if player_rect.right < WINDOW_WIDTH:
    #     player_rect.left += 0.2
    # display_surface.blit(player_surf, player_rect)
    # display_surface.blit(player.image, player.rect)

    allsprites.draw(display_surface)


    pygame.display.flip()

pygame.quit()