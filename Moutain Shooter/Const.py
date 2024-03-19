# c
import pygame

COLOR_ORANGE = (255, 128, 0)
COLOR_YELLOW = (255, 255, 128)
COLOR_WHITE = (255, 255, 255)

# M
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 2P - COMPETITIVE',
               'EXIT')

# w


WIN_WIDTH = 576
WIN_HEIGHT = 324

#E
EVENT_ENEMY = pygame.USEREVENT + 1
ENTITY_SPEED = {'level1bg0': 0,
                'level1bg1': 1,
                'level1bg2': 2,
                'level1bg3': 3,
                'level1bg4': 4,
                'level1bg5': 5,
                'level1bg6': 6,
                'player1':3,
                'player2':3,
                'enemy1': 2,
                'enemy2': 1
                }

PLAYER_KEY_UP = {'player1': pygame.K_UP,
                 'player2': pygame.K_w}

PLAYER_KEY_DOWN ={
                 'player1': pygame.K_DOWN,
                 'player2': pygame.K_s,}

PLAYER_KEY_RIGHT = { 'player1': pygame.K_RIGHT,
                     'player2': pygame.K_d}

PLAYER_KEY_LEFT = {'player1': pygame.K_LEFT,
                   'player2': pygame.K_a}
