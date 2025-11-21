import pygame
import sys
import random


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

GAP_SIZE = 150
GRAVITY = 0.25
JUMP_STRENGTH = -6


class Bird:
    def __init__(self):
        self.width = 40
        self.height = 30
        self.x = 50
        self.y = SCREEN_HEIGHT // 2
        self.velocity = 0
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

        # ДОПИСАТИ завантаження картинок

    def jump(self):
        ...

    def move(self):
        ...

    def draw(self, screen):
        # розрахунок центрування
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
        self.gap_y = random.randint(100, SCREEN_HEIGHT - 100 - GAP_SIZE)
        self.speed = 3
        self.passed = False

        # верхня труба
        self.top_rect = pygame.Rect(self.x, 0, self.width, self.gap_y)
        # нижня труба
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
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont('Arial', 24)
        self.big_font = pygame.font.SysFont('Arial', 40)

        # Дописати налаштування

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
                    # Логіка запуску гри
                    if event.key == pygame.K_SPACE:
                        # Дописати стрибок

                    # Дописати логіку перезапуску після Game Over


            # --- ЛОГІКА ГРИ (Працює тільки якщо гра почалась і не закінчилась) ---
            if self.game_started and not self.game_over:
                # Рух пташки, труб
                ...

            elif not self.game_started:
                # --- ЕКРАН ОЧІКУВАННЯ ---
                self.bird.draw(self.screen)  # Малюємо пташку, яка стоїть на місці

                start_text = self.big_font.render("Press SPACE", True, BLACK)
                start_text2 = self.big_font.render("to Start", True, BLACK)
                self.screen.blit(start_text, (SCREEN_WIDTH // 2 - 120, SCREEN_HEIGHT // 2 - 50))
                self.screen.blit(start_text2, (SCREEN_WIDTH // 2 - 80, SCREEN_HEIGHT // 2 + 10))

            else:
                # --- ЕКРАН СМЕРТІ ---
                txt_go = self.big_font.render("GAME OVER", True, BLACK)
                txt_r = self.font.render("Press 'R' to Restart", True, BLACK)
                self.screen.blit(txt_go, (SCREEN_WIDTH // 2 - 120, SCREEN_HEIGHT // 2 - 50))
                self.screen.blit(txt_r, (SCREEN_WIDTH // 2 - 110, SCREEN_HEIGHT // 2 + 10))

            # ДОПИСАТИ Інтерфейс



            

            pygame.display.flip()

        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    Game().run()
