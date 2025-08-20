import pygame.gfxdraw

pygame.init()

# Colors
BLACK = (18, 18, 19)
TEXT_WHITE = (248, 240, 240)
WHITE = (129, 131, 132)
GRAY = (58, 58, 60)
YELLOW = (181, 159, 59)
GREEN = (83, 141, 78)


class Words:
    def __init__(self, word_list, x, y):
        self.word_list = self.word_list_unique = word_list
        self.x = x
        self.y = y

        self.width = 810
        self.height = 250

        self.list_text = self.list_text_unique = ", ".join(word_list).upper()
        self.list_len = self.list_len_unique = len(word_list)

        self.reg_font = pygame.font.SysFont('Helvetica', 25)
        self.big_font = pygame.font.SysFont('Helvetica', 35)

        self.display_unique = False
        self.update = False

    def cycle_display_unique(self):
        self.display_unique = not self.display_unique
        self.update = True

    def update_word_list(self, word_list):
        # Update word list
        self.word_list = word_list
        self.word_list_unique = [
            word for word in word_list
            if len(set(word)) == len(word)
        ]

        self.list_text = ", ".join(word_list).upper()
        self.list_len = len(word_list)
        self.list_text_unique = ", ".join(self.word_list_unique).upper()
        self.list_len_unique = len(self.word_list_unique)

        self.update = True

    def draw(self, screen):
        if self.update:
            pygame.draw.rect(screen, BLACK, pygame.Rect(self.x, self.y, self.width, self.height))
            self.update = False

        if self.display_unique:
            list_text = self.list_text_unique
            list_len = self.list_len_unique
        else:
            list_text = self.list_text
            list_len = self.list_len

        # POSSIBLE WORDS text
        heading_text_surface = self.big_font.render(f"POSSIBLE WORDS: {list_len}", True, TEXT_WHITE)
        heading_text_x = self.x + (self.width - heading_text_surface.get_width()) // 2
        heading_text_y = -80 + self.y + (self.height - heading_text_surface.get_height()) // 2
        screen.blit(heading_text_surface, (heading_text_x, heading_text_y))

        # List of possible words
        list_text_surface = self.reg_font.render(list_text[:54], True, TEXT_WHITE)
        list_text_x = self.x + (self.width - list_text_surface.get_width()) // 2
        list_text_y = -10 + self.y + (self.height - list_text_surface.get_height()) // 2
        screen.blit(list_text_surface, (list_text_x, list_text_y))

        # + X more text
        if list_len > 8:
            more_text_surface = self.reg_font.render(f"+ {list_len-8} more", True, TEXT_WHITE)
            more_text_x = self.x + (self.width - more_text_surface.get_width()) // 2
            more_text_y = 30 + self.y + (self.height - more_text_surface.get_height()) // 2
            screen.blit(more_text_surface, (more_text_x, more_text_y))