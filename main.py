# importing stuff

import pygame
import time

# initializing pygame

pygame.init()

# defining variables

clock = pygame.time.Clock()
ver = "Beta 0.1"
autog = 0
coins = 0
display_width = 800
display_height = 600
white = (255, 255, 255)
black = (0, 0, 0)
grey = (128, 128, 128)
light_grey = (224, 224, 224)

# creating display and caption

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Memes cliker")


# defining functions

def autominer():
    global coins
    global autog
    time.sleep(0.1)
    coins = coins + autog


def draw_text(text, textcolor, rectcolor, x, y, fsize):
    font = pygame.font.Font('freesansbold.ttf', fsize)
    text = font.render(text, True, textcolor, rectcolor)
    text_rect = text.get_rect()
    text_rect.center = (x, y)
    gameDisplay.blit(text, text_rect)


def rectangle(display, color, x, y, w, h):
    pygame.draw.rect(display, color, (x, y, w, h))


def main_loop():
    global clock
    global autog
    global ver
    mong = 1
    cost = 50
    cost2 = 50
    global coins
    game_running = True
    while game_running:
        if game_running:
            autominer()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mopos = pygame.mouse.get_pos()
                if mopos >= (350, 0):
                    if mopos <= (450, 0):
                        coins += mong

                if mopos <= (800, 0):
                    if mopos >= (600, 0):
                        if coins >= cost:
                            coins = coins - cost
                            cost = cost * 1.5
                            mong += 1
                            cost = round(cost, 0)
                            print(f'{cost:.2f}')

                if mopos >= (50, 0):
                    if mopos <= (245, 0):
                        if coins >= cost2:
                            coins = coins - cost2
                            cost2 = cost2 * 1.5
                            autog = autog + 0.4
                            cost2 = round(cost2, 0)
                            print(f'{cost2:.2f}')

                if coins == 2147483647:
                    print("You Beat the game")

        # drawing stuff

        gameDisplay.fill(white)
        draw_text("Memes Clicker", black, white, 400, 100, 50)
        draw_text("you have " + str(f'{coins:.2f}') + " coins", black, white, 100, 50, 20)
        draw_text("upgrade 50*1.2", black, white, 650, 370, 20)
        draw_text("buy auto miner 50*1.2", black, white, 150, 370, 20)
        draw_text("Version: " + ver, black, white, 650, 50, 20)
        rectangle(gameDisplay, light_grey, 50, 400, 200, 300)
        rectangle(gameDisplay, black, 350, 250, 100, 100)
        rectangle(gameDisplay, light_grey, 550, 400, 200, 300)
        pygame.display.update()
        clock.tick(60)


# ending the program

main_loop()
pygame.quit()
quit()
