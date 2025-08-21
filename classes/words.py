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
        self.arrow_width = 40
        self.arrow_height = 40

        self.list_text = self.list_text_unique = ", ".join(word_list).upper()
        self.list_len = self.list_len_unique = len(word_list)

        self.list_concat_start = 0
        self.list_concat_end = 56

        self.right_arrow_visible = self.left_arrow_visible = False

        self.reg_font = pygame.font.SysFont('Helvetica', 25)
        self.big_font = pygame.font.SysFont('Helvetica', 35)

        self.display_unique = False
        self.update = False

    def cycle_display_unique(self):
        self.display_unique = not self.display_unique
        self.list_concat_start = 0
        self.list_concat_end = 56
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

        # Display the correct word list (normal or unique)
        if self.display_unique:
            list_text = self.list_text_unique
            list_len = self.list_len_unique
        else:
            list_text = self.list_text
            list_len = self.list_len

        # Right arrow button
        if self.list_concat_end <= len(list_text):
            self.right_arrow_visible = True
            pygame.draw.rect(screen, GRAY, pygame.Rect(self.x+740, self.y+95, self.arrow_width, self.arrow_height))
            right_arrow_surface = self.reg_font.render(">", True, TEXT_WHITE)
            right_arrow_text_x = 740 + self.x + (self.arrow_width - right_arrow_surface.get_width()) // 2
            right_arrow_text_y = 95 + self.y + (self.arrow_height - right_arrow_surface.get_height()) // 2
            screen.blit(right_arrow_surface, (right_arrow_text_x, right_arrow_text_y))
        else:
            self.right_arrow_visible = False

        # Left arrow button
        if self.list_concat_start > 0:
            self.left_arrow_visible = True
            pygame.draw.rect(screen, GRAY, pygame.Rect(self.x+30, self.y+95, self.arrow_width, self.arrow_height))
            left_arrow_surface = self.reg_font.render("<", True, TEXT_WHITE)
            left_arrow_text_x = 30 + self.x + (self.arrow_width - left_arrow_surface.get_width()) // 2
            left_arrow_text_y = 95 + self.y + (self.arrow_height - left_arrow_surface.get_height()) // 2
            screen.blit(left_arrow_surface, (left_arrow_text_x, left_arrow_text_y))
        else:
            self.left_arrow_visible = False

        # POSSIBLE WORDS text
        heading_text_surface = self.big_font.render(f"POSSIBLE WORDS: {list_len}", True, TEXT_WHITE)
        heading_text_x = self.x + (self.width - heading_text_surface.get_width()) // 2
        heading_text_y = -80 + self.y + (self.height - heading_text_surface.get_height()) // 2
        screen.blit(heading_text_surface, (heading_text_x, heading_text_y))

        # List of possible words
        list_text_surface = self.reg_font.render(list_text[self.list_concat_start:self.list_concat_end-2], True, TEXT_WHITE)
        list_text_x = self.x + (self.width - list_text_surface.get_width()) // 2
        list_text_y = -10 + self.y + (self.height - list_text_surface.get_height()) // 2
        screen.blit(list_text_surface, (list_text_x, list_text_y))

    def handle_event(self, event):
        mouse_pos = pygame.mouse.get_pos()

        # Right arrow
        if self.right_arrow_visible and (self.x+740) < mouse_pos[0] < (self.x+740) + self.arrow_width \
                and (self.y+95) < mouse_pos[1] < (self.y+95) + self.arrow_height:
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.list_concat_start = self.list_concat_end
                    self.list_concat_end += 56
                    self.update = True

        # Left arrow
        elif self.left_arrow_visible and (self.x+30) < mouse_pos[0] < (self.x+30) + self.arrow_width \
                and (self.y+95) < mouse_pos[1] < (self.y+95) + self.arrow_height:
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.list_concat_end = self.list_concat_start
                    self.list_concat_start -= 56
                    self.update = True
