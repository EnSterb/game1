# main.py
import pygame
import sys

pygame.init()

# Настройки экрана
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Clicker")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Шрифты
font = pygame.font.SysFont(None, 48)

# Игровые переменные
score = 0
click_value = 1

# Кнопка
button_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - 50, 200, 100)

clock = pygame.time.Clock()

# Основной цикл
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                score += click_value

    # Отрисовка
    screen.fill(WHITE)

    # Кнопка
    pygame.draw.rect(screen, (0, 128, 255), button_rect)
    click_text = font.render("Клик!", True, WHITE)
    screen.blit(click_text, (button_rect.x + 50, button_rect.y + 25))

    # Очки
    score_text = font.render(f"Очки: {score}", True, BLACK)
    screen.blit(score_text, (30, 30))

    pygame.display.flip()
    clock.tick(60)
