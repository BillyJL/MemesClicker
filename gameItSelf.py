import pygame
import time
pygame.init()

clock = pygame.time.Clock()
ver = "early alpha 0.2"
autog = 0
coins = 0
realPrise = 50
gameDisplay = pygame.display.set_mode((800, 600))
gameDisplay.fill((255, 255, 255))
pygame.display.set_caption("Memes Clicker 0.2")
pygame.display.set_icon(pygame.image.load('.idea\icon.png'))


font1 = pygame.font.SysFont('arial', 55)
font2 = pygame.font.SysFont('arial', 25)
green = (0, 153, 0)
brightGreen = (0, 255, 0)
black = (0, 0, 0)
grey = (128, 128, 128)
light_grey = (224, 224, 224)
white = (255, 255, 255)
rectWidth = 100
rectHeight = 60
mainMenu = True
mainText = font1.render("Memes Clicker", 1, black)
version = font2.render("ver. 0.2", 1, black)
startButton = font2.render("start", 1, black)
menuButton = font2.render("options", 1, black)
exitButton = font2.render("exit", 1, black)

def button (x, y, w, h, action = None):
    click = pygame.mouse.get_pressed()
    if (x+w) > mopos[0] > x and (y+h) > mopos[1] > y:
        pygame.draw.rect(gameDisplay, brightGreen, (x, y, w, h))
        if click[0] == 1 and action != None:
            if action == "play":
                main_loop()
                quit()
            elif action == "options":
                quit()
            elif action == "exit":
                quit()

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
                quit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                #main char
                mopos = pygame.mouse.get_pos()
                if 350 <= mopos[0] <= 450 and 250 <= mopos[1] <= 350:
                    coins += mong
                    
                # click multipler
                if 600 <= mopos[0] <= 700 and 415 <= mopos[1] <= 515:
                    if coins >= cost:
                        coins = coins - cost
                        cost = cost * 1.5
                        mong += 1
                        cost = round(cost, 0)
                        
                # autominer
                if 100 <= mopos[0] <= 200 and 415 <= mopos[1] <= 515:
                    if coins >= cost2:
                        coins = coins - cost2
                        cost2 = cost2 * 1.5
                        autog = autog + 0.4
                        cost2 = round(cost2, 0)

                if coins == 13371488:
                    print("You Beat the game")
                # ця частина з перемогою не робоча

        gameDisplay.fill(white)
        draw_text("Memes Clicker", black, white, 400, 100, 50)
        draw_text("you have " + str(f'{coins:.2f}') + " coins", black, white, 200, 50, 20)
        draw_text("buy click multiplier", black, white, 650, 370, 20)
        draw_text(str(f'{cost:.2f}' + " coins"), black, white, 650, 390, 20)
        draw_text("buy auto miner", black, white, 147, 370, 20)
        draw_text(str(f'{cost2:.2f}') + " coins", black, white, 150, 390, 20)
        draw_text("Version: " + ver, black, white, 650, 50, 20)
        rectangle(gameDisplay, light_grey, 100, 415, 100, 100)
        rectangle(gameDisplay, black, 350, 250, 100, 100)
        rectangle(gameDisplay, light_grey, 600, 415, 100, 100)
        pygame.display.update()
        clock.tick(60)

while mainMenu:
    mopos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    gameDisplay.blit(mainText, (215, 20))
    gameDisplay.blit(version, (515, 47))
    pygame.draw.rect(gameDisplay, black, (150, 150, rectWidth, rectHeight))
    pygame.draw.rect(gameDisplay, black, (350, 150, rectWidth, rectHeight))
    pygame.draw.rect(gameDisplay, black, (550, 150, rectWidth, rectHeight))
    pygame.draw.rect(gameDisplay, green, (152, 152, (rectWidth-4), (rectHeight-4)))
    pygame.draw.rect(gameDisplay, green, (352, 152, (rectWidth-4), (rectHeight-4)))
    pygame.draw.rect(gameDisplay, green, (552, 152, (rectWidth-4), (rectHeight-4)))
    button(152, 152, (rectWidth-4), (rectHeight-4), "play")
    button(352, 152, (rectWidth-4), (rectHeight-4), "options")
    button(552, 152, (rectWidth-4), (rectHeight-4), "exit")
    gameDisplay.blit(startButton, (178, 165))
    gameDisplay.blit(menuButton, (367, 165))
    gameDisplay.blit(exitButton, (583, 165))
    pygame.display.update()
