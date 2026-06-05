import pygame

def move_player(isForward, player, dt):
    movement = pygame.Vector2()
    movement.from_polar((300 * dt, player.angle))

    if isForward:
        player.pos += movement
    else:
        player.pos -= movement

def rotate_player(isLeft, player, dt):
    if isLeft: # vertical screen is inverted... why bruv
        player.angle -= dt * 120 
    else:
        player.angle += dt * 120

    # transform the figure once we have one