import pygame
import sys

pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600

# Colors
BG_COLOR = (33, 124, 66)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BUTTON_COLOR = (0, 10, 180)
BUTTON_HOVER_COLOR = (149, 168, 50)

# Fonts
font_large = pygame.font.SysFont('Roboto', 36)
font_medium = pygame.font.SysFont('Roboto', 24)

# Initialize the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("ElementAI")

# Game state
game_state = "MENU"  # Possible states: "MENU", "DIFFICULTY_SELECT", "GAME"

# Button class
class Button:
    def __init__(self, text, x, y, width, height, callback):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.color = BUTTON_COLOR
        self.callback = callback

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        draw_text(self.text, font_medium, WHITE, screen, self.rect.centerx, self.rect.centery)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.callback()

    def check_hover(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.color = BUTTON_HOVER_COLOR
        else:
            self.color = BUTTON_COLOR

# Function to display text on screen
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)

# Button callback functions
def start_game():
    global game_state
    game_state = "DIFFICULTY_SELECT"

def quit_game():
    global running
    running = False

def set_easy():
    global game_state
    print("Starting game with EASY difficulty")
    game_state = "GAME"

def set_medium():
    global game_state
    print("Starting game with MEDIUM difficulty")
    game_state = "GAME"

def set_hard():
    global game_state
    print("Starting game with HARD difficulty")
    game_state = "GAME"

def go_back_to_menu():
    global game_state
    game_state = "MENU"

# Menu buttons
menu_buttons = [
    Button("Start Game", screen_width // 2 - 100, screen_height // 2 - 50, 200, 50, start_game),
    Button("Quit", screen_width // 2 - 100, screen_height // 2 + 50, 200, 50, quit_game)
]

# Difficulty selection buttons
difficulty_buttons = [
    Button("Easy", screen_width // 2 - 100, screen_height // 2 - 70, 200, 50, set_easy),
    Button("Medium", screen_width // 2 - 100, screen_height // 2, 200, 50, set_medium),
    Button("Hard", screen_width // 2 - 100, screen_height // 2 + 70, 200, 50, set_hard),
    Button("Back", screen_width // 2 - 100, screen_height // 2 + 140, 200, 50, go_back_to_menu)
]

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if game_state == "MENU":
            for button in menu_buttons:
                button.handle_event(event)
        elif game_state == "DIFFICULTY_SELECT":
            for button in difficulty_buttons:
                button.handle_event(event)

    screen.fill(BG_COLOR)

    if game_state == "MENU":
        for button in menu_buttons:
            button.check_hover()
            button.draw(screen)
    elif game_state == "DIFFICULTY_SELECT":
        for button in difficulty_buttons:
            button.check_hover()
            button.draw(screen)
    elif game_state == "GAME":
        draw_text("Game in progress...", font_large, WHITE, screen, screen_width // 2, screen_height // 2)

    pygame.display.flip()

pygame.quit()
sys.exit()
