import pygame.gfxdraw

pygame.init()

# Colors
BLACK = (18, 18, 19)
TEXT_WHITE = (248, 240, 240)
WHITE = (129, 131, 132)
GRAY = (58, 58, 60)
YELLOW = (181, 159, 59)
GREEN = (83, 141, 78)


class Letter:
    def __init__(self, letter, x, y, left_click, right_click):
        self.letter = letter
        self.x = x
        self.y = y
        self.left_click = left_click
        self.right_click = right_click

        self.width = 70
        self.height = 90
        self.font = pygame.font.SysFont('Neue Helvetica', 50)
        self.color = WHITE

    def cycle_color(self):
        if self.color == WHITE:
            self.color = GRAY
        elif self.color == GRAY:
            self.color = WHITE
        else:
            self.color = WHITE

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

    def get_letter(self):
        return self.letter

    def draw(self, screen):
        # Render button rectangle
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, self.width, self.height), border_radius=10)

        # Render the text
        text_surface = self.font.render(self.letter, True, TEXT_WHITE)
        text_x = self.x + (self.width - text_surface.get_width()) // 2
        text_y = self.y + (self.height - text_surface.get_height()) // 2
        screen.blit(text_surface, (text_x, text_y))

    def handle_event(self, event):
        mouse_pos = pygame.mouse.get_pos()

        if self.x < mouse_pos[0] < self.x + self.width and self.y < mouse_pos[1] < self.y + self.height:
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 3:
                    self.cycle_color()
                    self.right_click(self.letter, self.color)  # update_gray_letters
                elif event.button == 1:
                    self.color = GRAY
                    self.left_click(self.letter)  # add_letter_to_slot
