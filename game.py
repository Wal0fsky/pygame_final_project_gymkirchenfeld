import pygame
from logic import move_player, rotate_player

pygame.init() # source: https://www.youtube.com/watch?v=dQw4w9WgXcQ&list=RDdQw4w9WgXcQ&start_radio=1
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

class Player:
    def __init__(self):
        self.angle = 0
        self.pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

player = Player()

while running: # game loop cycle
    dt = clock.tick(60) / 1000
    
    
    for event in pygame.event.get(): # event listener
        if event.type == pygame.QUIT: # player pressed "X"
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    pygame.draw.circle(screen, "red", player.pos, 40) # GENERATE IMAGE HERE

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        move_player(True, player, dt)
    if keys[pygame.K_s]:
        move_player(False, player, dt)
    if keys[pygame.K_a]:
        angle = rotate_player(True, player, dt)
    if keys[pygame.K_d]:
        angle = rotate_player(False, player, dt)

    pygame.display.flip() # pygame generates stuff on a hidden layer and then swaps it to the layer we see so it avoids screen flickering. This allows us to see the stuff after a frame

pygame.quit()

