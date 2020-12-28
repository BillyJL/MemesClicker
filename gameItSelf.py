import time
import pygame
pygame.init()


clock = pygame.time.Clock()
autog = 0
coins = 0
cost = 50
cost2 =50
cost_wojak = 1575
cost_cheems = 1575
pers = 0
gameDisplay = pygame.display.set_mode((800, 600))
gameDisplay.fill((255, 255, 255))
pygame.display.set_caption("Memes Clicker 0.47.3")
pygame.display.set_icon(pygame.image.load('img\icon.png'))

black = (0, 0, 0)
light_grey = (224, 224, 224)
white = (255, 255, 255)
spriteX = 275
spriteY = 175
#зображення "персонажів"
pepe_inactive = pygame.image.load('pers/pepe_inactive.png')
pepe_active = pygame.image.load('pers/pepe_active.png')
cheems_inactive = pygame.image.load('pers/cheems_inactive.png')
cheems_active = pygame.image.load('pers/cheems_active.png')
wojak_inactive = pygame.image.load('pers/wojak_inactive.png')
wojak_active = pygame.image.load('pers/wojak_active.png')
#зображення для індикаторів вибраного персонажа у магазині
pepe_not_activated = pygame.image.load('img/not_activated_pepe.png')
pepe_activated = pygame.image.load('img/activated_pepe.png')
cheems_not_activated = pygame.image.load('img/not_activated_cheems.png')
cheems_activated = pygame.image.load('img/activated_cheems.png')
wojak_not_activated = pygame.image.load('img/not_activated_wojak.png')
wojak_activated = pygame.image.load('img/activated_wojak.png')
pepe_magaz = pepe_activated
cheems_magaz = cheems_not_activated
wojak_magaz = wojak_not_activated
#"кнопки"
exit_button_img = pygame.image.load('img/menu_exit.png')
options_button_img = pygame.image.load('img/optimus_prime.png')
magaz_button_img = pygame.image.load('img/game_magaz.png')
booster_button_img1 = pygame.image.load('img/auto_buy.png')
booster_button_img2 = pygame.image.load('img/clicker_buy.png')
back_button_img = pygame.image.load('img/back_button.png')
cheat_img = pygame.image.load('img/cheat_button.png')

def textObjects(text, font):
    textSurface = font.render(text, True, (0, 0, 0))
    return textSurface, textSurface.get_rect()

def rectangle(display, color, x, y, w, h):
    pygame.draw.rect(display, color, (x, y, w, h))

def button(x, y, w, h, action = None):
    click = pygame.mouse.get_pressed()
    mopos = pygame.mouse.get_pos()
    pygame.draw.rect(gameDisplay, (0, 0, 0), (x, y, w, h))
    pygame.draw.rect(gameDisplay, (128, 128, 128), (x+2, y+2, w-4, h-4))  
    if x <= mopos[0] <= (x+w) and y <= mopos[1] <= (y+h):
        pygame.draw.rect(gameDisplay, (0, 0, 0), (x, y, w, h))
        pygame.draw.rect(gameDisplay, (230, 230, 230), (x+2, y+2, w-4, h-4))
        if click[0] == 1 and action != None:
            if action == "play":
                main_loop()
            elif action == "options":
                options()
            elif action == "exit":
                quit()
            elif action == "store":
                gameDisplay.fill(white)
                store()
            elif action == "main_menu":
                gameDisplay.fill(white)
                main_menu()
        
def autominer():
    global coins
    global autog
    time.sleep(0.1)
    coins = coins + autog


def draw_text(text, textcolor, x, y, fsize):
    font = pygame.font.Font('freesansbold.ttf', fsize)
    text = font.render(text, True, textcolor)
    text_rect = text.get_rect()
    text_rect.center = (x, y)
    gameDisplay.blit(text, text_rect)

def char_switch(pers):
    global sprite_active
    global sprite_inactive
    mopos = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if click[0] == 1:
        if pers == 0:
            sprite_inactive = pepe_inactive
            sprite_active = pepe_active
        elif pers == 1:
            sprite_inactive = cheems_inactive
            sprite_active = cheems_active
        elif pers == 2:
            sprite_inactive = wojak_inactive
            sprite_active = wojak_active
#options
def options():
    gameDisplay.fill(white)
    button(25, 25, 150, 150, "main_menu")
    gameDisplay.blit(back_button_img,(25,25))
    pygame.display.update()
    clock.tick(60)
        
#store
def store():
    global coins
    global pers
    global cost_cheems
    global cost_wojak
    global pepe_magaz
    global cheems_magaz
    global wojak_magaz
    while True:
        autominer()
        mopos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        for event in pygame.event.get():
            if click[0] == 1:
                    if 87.5 <= mopos[0] <= 237.5 and 275 <= mopos[1] <= 425:
                        pers = 0
                        pepe_magaz = pepe_activated
                        cheems_magaz = cheems_not_activated
                        wojak_magaz = wojak_not_activated
                    if 325 <= mopos[0] <= 475 and 275 <= mopos[1] <= 425:
                        if coins > cost_cheems:
                            pers = 1
                            coins -= cost_cheems
                            cost_cheems = 0
                            pepe_magaz = pepe_not_activated
                            cheems_magaz = cheems_activated
                            wojak_magaz = wojak_not_activated
                    if 562.5 <= mopos[0] <= 712.5 and 275 <= mopos[1] <= 425:
                        if coins > cost_wojak:
                            pers = 2
                            coins -= cost_wojak
                            cost_wojak = 0
                            pepe_magaz = pepe_not_activated
                            cheems_magaz = cheems_not_activated
                            wojak_magaz = wojak_activated
                        
        gameDisplay.fill(white)
        draw_text("you have " + str(f'{coins:.2f}') + " coins", black, 400, 50, 20)
        gameDisplay.blit(pepe_magaz,(87.5,275))
        gameDisplay.blit(cheems_magaz,(325,275))
        gameDisplay.blit(wojak_magaz,(562.5,275))
        draw_text("always with you", black, 150, 450, 20)
        draw_text(str(f'{cost_cheems:.2f}') + " coins", black, 400, 450, 20)
        draw_text(str(f'{cost_wojak:.2f}') + " coins", black, 650, 450, 20)
        button(25, 25, 150, 150, "play")
        gameDisplay.blit(back_button_img,(25,25))
        pygame.display.update()
        clock.tick(60)
        
#character
def main_char():
    global pers
    char_switch(pers)
    mopos = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    gameDisplay.blit(sprite_inactive,(spriteX,spriteY))
    if 275 <= mopos[0] <= 525 and 175 <= mopos[1] <= 425:
        rectangle(gameDisplay, (255, 255,255) ,275, 175,250, 250)
        gameDisplay.blit(sprite_active,(spriteX,spriteY))
        
#Main menu       
def main_menu():
    while True:
        global coins
        global clock
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        draw_text("Memes Clicker", (0, 0, 0), 400, 100, 50)
        button(75, 375, 150, 150, "exit")
        button(575, 375, 150, 150, "options")
        button(220, 180, 360, 100, "play")
        draw_text("start", (0, 0, 0), 400, 228, 45)
        gameDisplay.blit(exit_button_img,(75,375))
        gameDisplay.blit(options_button_img,(575,375))
        pygame.display.update()
        clock.tick(60)

#game
def main_loop():
    global clock
    global autog
    global ver
    global cost
    global cost2
    global pers
    char_switch(pers)
    mong = 1
    global coins
    game_running = True
    
    while game_running:
        if game_running:
            mopos = pygame.mouse.get_pos()
            autominer()
            gameDisplay.fill(white)
            main_char()

        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                quit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                #main char
                if 275 <= mopos[0] <= 525 and 175 <= mopos[1] <= 425:
                    coins += mong
                    main_char()

                # click multipler
                if 600 <= mopos[0] <= 700 and 415 <= mopos[1] <= 530:
                    if coins >= cost:
                        coins = coins - cost
                        cost = cost * 1.5
                        mong += 1
                        cost = round(cost, 0)
                        
                # autominer
                if 100 <= mopos[0] <= 200 and 415 <= mopos[1] <= 530:
                    if coins >= cost2:
                        coins = coins - cost2
                        cost2 = cost2 * 1.5
                        autog = autog + 0.4
                        cost2 = round(cost2, 0)
                if 0 <= mopos[0] <= 25 and 575 <= mopos[1] <= 600:
                    coins += 88005553535

        draw_text("you have " + str(f'{coins:.2f}') + " coins", black, 400, 50, 20)
        draw_text("buy click multiplier", black, 650, 370, 20)
        draw_text(str(f'{cost:.2f}' + " coins"), black, 650, 390, 20)
        draw_text("buy auto miner", black, 147, 370, 20)
        draw_text(str(f'{cost2:.2f}') + " coins", black, 150, 390, 20)
        button(25, 25, 150, 150, "main_menu")
        button(625, 25, 150, 150, "store")
        gameDisplay.blit(booster_button_img1,(75,400))
        gameDisplay.blit(booster_button_img2,(575,400))
        gameDisplay.blit(back_button_img,(25,25))
        gameDisplay.blit(magaz_button_img,(625,25))
        gameDisplay.blit(cheat_img,(0,575))
        pygame.display.update()
        clock.tick(60)
    
while True:
    main_menu()
