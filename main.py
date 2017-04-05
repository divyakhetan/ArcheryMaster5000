import pygame
import time

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

screen_width = 800
screen_height = 600
block_width = 100
block_height = 20
arrow_width = 5
arrow_height = 95

display = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("ARCHERY MASTER 5000")

clock = pygame.time.Clock()

pygame.init()

font = pygame.font.SysFont(None, 25)


def message_to_screen(msg, color):
    screen_text = font.render(msg, True, color)
    display.blit(screen_text, [screen_width / 2 - 200, screen_height / 2])


def gameLoop():
    block_x = 300
    block_y = 25
    block_speed = 10

    arrow_x = 400
    arrow_y = 500
    arrow_speed = 0

    trigger = 0
    chances = 0
    flag = 0

    gameExit = False
    gameWin = False
    gameThree = False

    while not gameExit:

        while gameWin == True:
            display.fill(white)
            message_to_screen("You Win! Play again? (c/q)", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameWin = False

                    if event.key == pygame.K_c:
                        gameLoop()

        while gameThree == True:
            display.fill(white)
            message_to_screen("Done with 3 tries, press c to continue or q to quit", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameThree = False

                    if event.key == pygame.K_c:
                        gameLoop()

        display.fill((255, 255, 255))
        trigger += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    arrow_speed = 20
                    flag = 1
                    chances += 1

        if trigger == 100:
            flag = 0
            trigger = 0
            arrow_y = 500
            arrow_speed = 0

        if chances > 3:
            gameThree = True

        if block_x < 5 or block_x > screen_width - block_width + 5:
            block_speed *= -1

        block_x += block_speed
        arrow_y -= arrow_speed

        # position set - > debug
        if arrow_y in range(block_y + block_height - arrow_height,
                            block_y + block_height) and block_x + 5 <= arrow_x <= (block_x + block_width - 5):
            print("hit")
            gameWin = True

        pygame.draw.rect(display, (255, 0, 0), [block_x, block_y, block_width, block_height])
        pygame.draw.rect(display, (0, 0, 0), [arrow_x, arrow_y, arrow_width, arrow_height])
        pygame.display.update()

        clock.tick(60)

    pygame.quit()
    quit()


gameLoop()
