import pygame

def move_player(isForward, player):
    movement = pygame.Vector2()
    movement.from_polar((300 * player.dt, player.angle))

    if isForward:
        player.pos += movement
    else:
        player.pos -= movement

def rotate_player(isLeft, player):
    if isLeft:
        player.angle += player.dt * 120
    else:
        player.angle -= player.dt * 120

    # Transform the figure once we have one