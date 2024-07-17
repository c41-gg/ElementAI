import pygame
from constants import BACKGROUND_MENU, button_new_game_image, button_exit_image, WHITE, WIDTH, WIN, HEIGHT

pygame.init()

ratio = 2
button_width = int(1076 / ratio)
button_height = int(520 / ratio)

BUTTON_COLOR = (0, 10, 180)
BUTTON_HOVER_COLOR = (149, 168, 50)

# Fonts
font_large = pygame.font.SysFont('Roboto', 36)
font_medium = pygame.font.SysFont('Roboto', 24)

# Game state
game_state = "MENU"  # Possible states: "MENU", "DIFFICULTY_SELECT", "GAME"


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
    pygame.quit()
    quit()


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


class Button:
    def __init__(self, text, x, y, width, height, callback):
        self.x = x
        self.y = y
        self.text = text
        self.width = width
        self.height = height
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
                
    def isOver(self, mouse_position):
        if self.draft.collidepoint(mouse_position):
            return True
        return False

    def check_hover(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.color = BUTTON_HOVER_COLOR
        else:
            self.color = BUTTON_COLOR


# Menu buttons
menu_buttons = [
    Button("Start Game", WIDTH // 2 - 100, HEIGHT // 2 - 50, 200, 50, start_game),
    Button("Quit", WIDTH // 2 - 100, HEIGHT // 2 + 50, 200, 50, quit_game)
]

# Difficulty selection buttons
difficulty_buttons = [
    Button("Easy", WIDTH // 2 - 100, HEIGHT // 2 - 70, 200, 50, set_easy),
    Button("Medium", WIDTH // 2 - 100, HEIGHT // 2, 200, 50, set_medium),
    Button("Hard", WIDTH // 2 - 100, HEIGHT // 2 + 70, 200, 50, set_hard),
    Button("Back", WIDTH // 2 - 100, HEIGHT // 2 + 140, 200, 50, go_back_to_menu)
]


def menu_start():
    global running, game_state
    running = True
    game_state = "MENU"
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()

            if game_state == "MENU":
                for button in menu_buttons:
                    button.handle_event(event)
            elif game_state == "DIFFICULTY_SELECT":
                for button in difficulty_buttons:
                    button.handle_event(event)

        WIN.blit(BACKGROUND_MENU, (0, 0))

        if game_state == "MENU":
            for button in menu_buttons:
                button.check_hover()
                button.draw(WIN)
        elif game_state == "DIFFICULTY_SELECT":
            for button in difficulty_buttons:
                button.check_hover()
                button.draw(WIN)
        elif game_state == "GAME":
            return

        pygame.display.flip()


def menu_end():
    from player import Player
    from constants import WIN, WIDTH, BEIGE

    player_list_chair = Player.player_list_chair
    for player in player_list_chair:
        if player.stack != 0:
            winner = player.name
    WIN.blit(BACKGROUND_MENU, (0, 0))
    font = pygame.font.SysFont('Roboto', 60)
    text = font.render(winner+' won the game', True, BEIGE)
    WIN.blit(text, ((WIDTH - text.get_width()) // 2, 100))
    button_new_game = Button((WIDTH - button_width)//2, 300, button_new_game_image, button_width, button_height)
    button_exit = Button((WIDTH - button_width)//2, 500, button_exit_image, button_width, button_height)
    rebuy = False
    pause_menu = True
    while pause_menu:
        button_exit.draw(WIN)
        button_new_game.draw(WIN)

        for event in pygame.event.get():
            mouse_position = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_new_game.isOver(mouse_position):
                    rebuy = True
                    pause_menu = False
                if button_exit.isOver(mouse_position):
                    run = False
                    pygame.quit()
                    quit()

        pygame.display.flip()
    return rebuy