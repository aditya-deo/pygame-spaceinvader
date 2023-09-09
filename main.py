import random
import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
running = True

pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)
spaceship_size = (64, 64)
monster1_size = (64, 64)

# player
playerImg = pygame.image.load("rocket.png")
playerImg = pygame.transform.scale(playerImg, spaceship_size)

enemyImg1 = pygame.image.load("monster1.png")
enemyImg1 = pygame.transform.scale(enemyImg1, monster1_size)

playerX = 368
playerY = 480
playerX_change = 0


monster1X = random.randint(32, 768)
monster1Y = 50


def player(x, y):
    screen.blit(playerImg, (x, y))


def monster1(x, y):
    screen.blit(enemyImg1, (x, y))


# game loop
while running:
    screen.fill((0, 0, 0))  # setting the color of the screen before everything else

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            elif event.key == pygame.K_RIGHT:
                playerX_change = 0.3
        elif event.type == pygame.KEYUP:
            playerX_change = 0
    playerX += playerX_change
    if playerX < 0:
        playerX = 0
    elif playerX > 736:
        playerX = 736

    monster1(monster1X, monster1Y)
    player(playerX, playerY)
    pygame.display.update()
