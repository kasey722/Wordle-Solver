import pygame.gfxdraw

pygame.init()

# Colors
BLACK = (18, 18, 19)
TEXT_WHITE = (248, 240, 240)
WHITE = (129, 131, 132)
GRAY = (58, 58, 60)
YELLOW = (181, 159, 59)
GREEN = (83, 141, 78)


class Slot:
    def __init__(self, slot_number, x, y, callback):
        self.slot_number = slot_number
        self.x = x
        self.y = y
        self.callback = callback

        self.letter = ""
        self.width = 90
        self.height = 90
        self.font = pygame.font.SysFont('Neue Helvetica', 70)
        self.color = BLACK

    def cycle_color(self):
        if self.color == GRAY:
            self.color = YELLOW
        elif self.color == YELLOW:
            self.color = GREEN
        elif self.color == GREEN:
            self.color = GRAY
        else:
            self.color = GRAY

    def get_slot_number(self):
        return self.slot_number

    def get_position(self):
        return self.x, self.y

    def get_letter(self):
        return self.letter

    def set_letter(self, letter):
        self.letter = letter
        self.color = GRAY

    def get_color(self):
        return self.color

    def draw(self, screen):
        # Render rectangle border
        if self.color == BLACK:
            pygame.draw.rect(screen, GRAY, pygame.Rect(self.x, self.y, self.width, self.height), 4)
        else:
            pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, self.width, self.height), 4)

        # Render rectangle fill
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x+4, self.y+4, self.width-8, self.height-8))

        # Render the text
        text_surface = self.font.render(self.letter, True, TEXT_WHITE)
        text_x = self.x + (self.width - text_surface.get_width()) // 2
        text_y = self.y + (self.height - text_surface.get_height()) // 2
        screen.blit(text_surface, (text_x, text_y))

    def handle_event(self, event):
        if self.letter != "":
            mouse_pos = pygame.mouse.get_pos()

            if self.x < mouse_pos[0] < self.x + self.width and self.y < mouse_pos[1] < self.y + self.height:
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 3:  # Right click
                        self.cycle_color()
                        self.callback(self.letter, self.color)  # set_slot_letter_color
                    elif event.button == 1:  # Left click
                        self.callback(self.letter, GRAY)  # set_slot_letter_color
                        self.letter = ""
                        self.color = BLACK
