import pygame
import sys

pygame.init()

# Screen dimensions
screen_width = 900
screen_height = 700

BG_COLOR = (33, 124, 66)

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("ElementAI")

# Load card images
back_image = pygame.image.load("assests/images/cards/back.png")
front_image = pygame.image.load("assests/images/cards/f_2.png")

# Resize the images
card_width, card_height = 300, 350
back_image = pygame.transform.scale(back_image, (card_width, card_height))
front_image = pygame.transform.scale(front_image, (card_width, card_height))

# Card class
class Card:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dragging = False
        self.show_front = False

    def draw(self, screen):
        if self.show_front:
            screen.blit(front_image, (self.x, self.y))
        else:
            screen.blit(back_image, (self.x, self.y))

    def is_mouse_over(self, mouse_x, mouse_y):
        return self.x <= mouse_x <= self.x + card_width and self.y <= mouse_y <= self.y + card_height

# Create a deck of cards
deck = [Card(screen_width // 2 - card_width // 2, screen_height // 2 - card_height // 2) for _ in range(5)]

# Main game loop
running = True
dragged_card = None
mouse_offset_x = 0
mouse_offset_y = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            for card in reversed(deck):
                if card.is_mouse_over(mouse_x, mouse_y):
                    if event.button == 1:  # Left mouse button
                        card.dragging = True
                        mouse_offset_x = card.x - mouse_x
                        mouse_offset_y = card.y - mouse_y
                        dragged_card = card
                    elif event.button == 3:  # Right mouse button
                        card.show_front = not card.show_front
                    break
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # Left mouse button
                if dragged_card:
                    dragged_card.dragging = False
                    dragged_card = None
        elif event.type == pygame.MOUSEMOTION:
            if dragged_card and dragged_card.dragging:
                mouse_x, mouse_y = event.pos
                dragged_card.x = mouse_x + mouse_offset_x
                dragged_card.y = mouse_y + mouse_offset_y

    screen.fill(BG_COLOR)

    for card in deck:
        card.draw(screen)

    pygame.display.flip()

pygame.quit()
sys.exit()

