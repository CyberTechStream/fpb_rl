import pygame
import sys
import random

# --- КОНСТАНТИ ---
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
FPS = 60

# Кольори
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 50, 50)
SKY_BLUE = (135, 206, 235)
GREEN = (34, 139, 34)
DARK_GREEN = (0, 100, 0)

# Налаштування
GAP_SIZE = 150
GRAVITY = 0.25
JUMP_STRENGTH = -6

# --- КЛАСИ ---
class Bird:
    def __init__(self):
        self.width = 40
        self.height = 30
        self.x = 50
        self.y = SCREEN_HEIGHT // 2
        self.velocity = 0
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        # дописати картинки




    def jump(self):
        ...

    def move(self):
        ...

    def draw(self, screen):
        center_x = self.rect.x + (self.rect.width // 2)
        center_y = self.rect.y + (self.rect.height // 2)

        rot_width = self.rotated_image.get_width()
        rot_height = self.rotated_image.get_height()

        blit_x = center_x - (rot_width // 2)
        blit_y = center_y - (rot_height // 2)

        screen.blit(self.rotated_image, (blit_x, blit_y))

    def reset_position(self):
        ...


class Pipe:
    def __init__(self):
        self.width = 60
        self.x = SCREEN_WIDTH
        # відст. між трубами
        self.gap_y = random.randint(100, SCREEN_HEIGHT - 100 - GAP_SIZE)
        self.speed = 3
        self.passed = False
        # врех. та нижн. труби
        self.top_rect = pygame.Rect(self.x, 0, self.width, self.gap_y)
        self.bottom_rect = pygame.Rect(self.x, self.gap_y + GAP_SIZE, self.width,
                                       SCREEN_HEIGHT - (self.gap_y + GAP_SIZE))

    def move(self):
        ...

    def draw(self, screen):
        ...


# --- ГОЛОВНИЙ КЛАС ---
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Flappy Bird")
        # дописати



    def reset_round(self):
        ...

    def run(self):
        while self.running:
            self.clock.tick(FPS)
            self.screen.fill(SKY_BLUE)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    ...
                    # дописати

            if self.game_started and not self.game_over:
                 # дописати

            elif not self.game_started:
                self.bird.draw(self.screen)

                start_text = self.big_font.render("Press SPACE", True, BLACK)
                start_text2 = self.big_font.render("to Start", True, BLACK)

                self.screen.blit(start_text, (SCREEN_WIDTH // 2 - 120, SCREEN_HEIGHT // 2 - 50))
                self.screen.blit(start_text2, (SCREEN_WIDTH // 2 - 80, SCREEN_HEIGHT // 2 + 10))

            else:
                txt_go = self.big_font.render("GAME OVER", True, BLACK)
                txt_r = self.font.render("Press 'R' to Restart", True, BLACK)
                self.screen.blit(txt_go, (SCREEN_WIDTH // 2 - 120, SCREEN_HEIGHT // 2 - 50))
                self.screen.blit(txt_r, (SCREEN_WIDTH // 2 - 110, SCREEN_HEIGHT // 2 + 10))

            score_surf = self.font.render(f"Score: {self.score}", True, WHITE)
            score_shadow = self.font.render(f"Score: {self.score}", True, BLACK)
            self.screen.blit(score_shadow, (12, 12))
            self.screen.blit(score_surf, (10, 10))

            pygame.display.flip()

        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    Game().run()
