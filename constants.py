import pygame
from os import path
from cards import Card


pygame.init()

FPS = 1
HEIGHT = 720
WIDTH = 1280
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BEIGE = (225, 198, 153)
RED = (255, 0, 0)
SB, BB = 25, 50

# Load images
images_direction = path.join(path.dirname(__file__), 'assests')

# Background game
BACKGROUND = pygame.image.load(path.join(images_direction, 'battleground_bg.jpg')).convert()
BACKGROUND = pygame.transform.scale(BACKGROUND, (WIDTH, HEIGHT))

# Background menu
BACKGROUND_MENU = pygame.image.load(path.join(images_direction, 'menu_bg.jpg')).convert()
BACKGROUND_MENU = pygame.transform.scale(BACKGROUND_MENU, (WIDTH, HEIGHT))

# Button menu
button_new_game_image = pygame.image.load(path.join(images_direction, 'bg_menu.png')).convert_alpha()
button_exit_image = pygame.image.load(path.join(images_direction, 'bg_menu.png')).convert_alpha()

# Game button
button_image = pygame.image.load(path.join(images_direction, 'bg_menu.png')).convert_alpha()
button_image.set_colorkey(WHITE)

# Label player
label_player_image = pygame.image.load(path.join(images_direction, 'bg_name.png')).convert_alpha()
label_player_image.set_colorkey(WHITE)


# < Cards

deck = ['MB', 'MG', 'MR', 'MY', 'KB', 'KG', 'KR', 'KY', 'RB', 'RG', 'RR', 'RY']

cards_list_images = ['MB.png', 'MG.png', 'MR.png', 'MY.png', 'KB.png', 'KG.png', 'KR.png', 'KY.png', 'RB.png', 'RG.png', 'RR.png', 'RY.png']

cards_images = []
for img in cards_list_images:
    card_img = pygame.image.load(path.join(images_direction, img)).convert_alpha()
    cards_images.append(card_img)

# Dictionary with cards object
cards_object = {}
for i in range(len(cards_images)):
    name = deck[i]
    cards_object[name] = Card(cards_images[i])

# Opponent cards
card_reverse_image = pygame.image.load(path.join(images_direction, 'back.png')).convert_alpha()
cards_object['reverse_1'] = Card(card_reverse_image)
cards_object['reverse_2'] = Card(card_reverse_image)



