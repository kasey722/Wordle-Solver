import pygame.gfxdraw

pygame.init()

# Colors
BLACK = (18, 18, 19)
TEXT_WHITE = (248, 240, 240)
WHITE = (129, 131, 132)
GRAY = (58, 58, 60)
YELLOW = (181, 159, 59)
GREEN = (83, 141, 78)


class Reset:
    def __init__(self, x, y, callback):
        self.x = x
        self.y = y
        self.callback = callback

        self.width = 110
        self.height = 90
        self.font = pygame.font.SysFont('Neue Helvetica', 30)

    def draw(self, screen):
        # Render button rectangle
        pygame.draw.rect(screen, WHITE, pygame.Rect(self.x, self.y, self.width, self.height), border_radius=10)

        # Render the text
        text_surface = self.font.render("RESET", True, TEXT_WHITE)
        text_x = self.x + (self.width - text_surface.get_width()) // 2
        text_y = self.y + (self.height - text_surface.get_height()) // 2
        screen.blit(text_surface, (text_x, text_y))

    def handle_event(self, event):
        mouse_pos = pygame.mouse.get_pos()

        if self.x < mouse_pos[0] < self.x + self.width and self.y < mouse_pos[1] < self.y + self.height:
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:  # left click
                    self.callback()  # reset

