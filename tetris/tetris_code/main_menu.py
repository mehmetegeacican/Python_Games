import pygame
import pygame_menu
from figures import *
from tetris import *
from main import *


def start_game():
    main()


pygame.init()
surface = pygame.display.set_mode((400, 500))

menu = pygame_menu.Menu(500, 400, 'Welcome to Tetris',theme=pygame_menu.themes.THEME_DARK)
menu.add_button('Play', start_game)
menu.add_button('Quit', pygame_menu.events.EXIT)
menu.mainloop(surface)

