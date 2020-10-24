import pygame
import random
from win32api import GetSystemMetrics
from pygame.locals import *
import os


pygame.init()
display_width = GetSystemMetrics(0)
display_height = GetSystemMetrics(1)

gameDisplay = pygame.display.set_mode((display_width, display_height), RESIZABLE)
pygame.display.set_caption('Snake Game')

black = (0, 0, 0)
# brown = (230, 160, 98)
flame = (226, 88, 34)
snake_width = 73
red = (220,20,60)
green = (34,139,34)

bright_red = (255, 0, 0)
bright_green = (50,205,50)

clock = pygame.time.Clock()
crashed = False
snake_img = pygame.image.load('snake.png')
background_image = pygame.image.load("grass.jpg").convert()


def things1(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def things2(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])


def snake(x, y):
    gameDisplay.blit(snake_img, (x, y))


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def crash():
    largeText = pygame.font.SysFont("freesansbold.ttf", 100)
    TextSurf, TextRect = text_objects("You Died", largeText)
    TextRect.center = ((display_width / 2), (display_height / 4))
    gameDisplay.blit(TextSurf, TextRect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("Restart Game", 540, 330, 200, 50, red, bright_red, game_loop)
        # button("Exit", 550, 450, 100, 50, red, bright_red, quitgame)

        pygame.display.update()
        clock.tick(15)


def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))
    smallText = pygame.font.SysFont("freesansbold.ttf", 40)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(textSurf, textRect)


def quitgame():
    pygame.quit()
    quit()


def unpause():
    global pause
    pause = False


def paused():
    largeText = pygame.font.SysFont("freesansbold.ttf", 115)
    TextSurf, TextRect = text_objects("Paused", largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("Unpause", 540, 450, 200, 50, green, bright_green, unpause)
        # button("Exit", 550, 450, 100, 50, red, bright_red, quitgame)

        pygame.display.update()
        clock.tick(15)

def game_intro():
    intro = True
    x = display_width
    y = display_height
    gameDisplay.blit(background_image, [0, 0])
    logo = pygame.image.load(os.path.join("logo.png")).convert()
    logo_rect = logo.get_rect(center = gameDisplay.get_rect().center)
    font = pygame.font.Font('freesansbold.ttf', 32)

    while intro:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.blit(background_image, [0, 0])
        # largeText = pygame.font.SysFont("freesansbold.ttf", 100)
        # TextSurf, TextRect = text_objects("SNAKE & FIRE !!!", largeText)
        # TextRect.center = ((display_width / 2), (display_height / 4))

        title_text = font.render('SNAKE & FIRE !!!', True, red, flame)
        textRect = title_text.get_rect()
        textRect.center = ((display_width / 2), (display_height / 4))
        gameDisplay.blit(title_text, textRect)

        button("Start Game", 540, 450, 200, 50, green, bright_green, game_loop)
        # button("Finish!!!", 550, 450, 100, 50, red, bright_red, quitgame)
        gameDisplay.blit(logo, logo_rect)
        pygame.display.update()
        clock.tick(15)
        mouse = pygame.mouse.get_pos()
        if 150 + 100 > mouse[0] > 150 and 450 + 50 > mouse[1] > 450:
            pygame.draw.rect(gameDisplay, bright_green, (150, 450, 100, 50))
        else:
            pygame.draw.rect(gameDisplay, green, (150, 750, 100, 50))

        smallText = pygame.font.Font("freesansbold.ttf", 20)
        textSurf, textRect = text_objects("Start Game", smallText)
        textRect.center = (640, 480)
        gameDisplay.blit(textSurf, textRect)
        # pygame.draw.rect(gameDisplay, red, (550, 450, 100, 50))
        pygame.display.update()
        clock.tick(15)


def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0

    thing1_startx = random.randrange(0, display_width)
    thing2_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 7
    thing_width = 100
    thing_height = 100

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change

        gameDisplay.blit(background_image, [0, 0])

        things1(thing1_startx, thing_starty, thing_width, thing_height, flame)
        things2(thing2_startx, thing_starty, thing_width, thing_height, flame)
        thing_starty += thing_speed
        snake(x, y)

        if x > display_width - snake_width or x < 0:
            gameExit = True

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing1_startx = random.randrange(0, display_width)
            thing2_startx = random.randrange(0, display_width)

        if y < thing_starty + thing_height:
            print('y crossover')

            if thing1_startx < x < thing1_startx + thing_width or thing1_startx < x + snake_width < thing1_startx + thing_width:
                print('x crossover')
                crash()
            elif thing2_startx < x < thing2_startx + thing_width or thing2_startx < x + snake_width < thing2_startx + thing_width:
                print('x crossover')
                crash()

        pygame.display.update()
        clock.tick(60)


game_intro()
game_loop()
pygame.quit()
quit()
