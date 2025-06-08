import pygame
import time
import random

pygame.init()

# Game window
width, height = 400, 400
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simple Snake")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

# Snake settings
snake_block = 10
snake_speed = 10
clock = pygame.time.Clock()

font = pygame.font.SysFont("Arial", 25)

def game():
    game_over = False
    x = width // 2
    y = height // 2
    dx = 0
    dy = 0

    snake = []
    length = 1

    food_x = random.randint(0, (width - snake_block) // 10) * 10
    food_y = random.randint(0, (height - snake_block) // 10) * 10

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx = -snake_block
                    dy = 0
                elif event.key == pygame.K_RIGHT:
                    dx = snake_block
                    dy = 0
                elif event.key == pygame.K_UP:
                    dy = -snake_block
                    dx = 0
                elif event.key == pygame.K_DOWN:
                    dy = snake_block
                    dx = 0

        x += dx
        y += dy

        if x < 0 or x >= width or y < 0 or y >= height:
            game_over = True

        win.fill(black)
        pygame.draw.rect(win, red, (food_x, food_y, snake_block, snake_block))

        head = [x, y]
        snake.append(head)
        if len(snake) > length:
            del snake[0]

        # Collision with self
        for block in snake[:-1]:
            if block == head:
                game_over = True

        for part in snake:
            pygame.draw.rect(win, green, (part[0], part[1], snake_block, snake_block))

        pygame.display.update()

        if x == food_x and y == food_y:
            food_x = random.randint(0, (width - snake_block) // 10) * 10
            food_y = random.randint(0, (height - snake_block) // 10) * 10
            length += 1

        clock.tick(snake_speed)

    # Game over message
    win.fill(black)
    msg = font.render("Game Over!", True, white)
    win.blit(msg, [width // 3, height // 2])
    pygame.display.update()
    time.sleep(2)
    pygame.quit()

game()