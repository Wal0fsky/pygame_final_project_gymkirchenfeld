import pygame
from logic import move_player, rotate_player

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

class Player:
    def __init__(self):
        self.dt = clock.tick(60) / 1000
        self.angle = 0
        self.pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
    dt = 0

player = Player()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    pygame.draw.circle(screen, "red", player.pos, 40) # GENERATE IMAGE HERE

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        move_player(True, player)
    if keys[pygame.K_s]:
        move_player(False, player)
    if keys[pygame.K_a]:
        angle = rotate_player(True, player)
    if keys[pygame.K_d]:
        angle = rotate_player(False, player)

    # flip() the display to put your work on screen
    pygame.display.flip()

pygame.quit()

