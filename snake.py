import pygame
import time
import random

# Set the speed of the snake via a variable
speed = 15

# create variables for the window sizes
window_x = 720
window_y = 480

# define the colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(232, 72, 29)
light_green = pygame.Color(171, 215, 82)
dark_green = pygame.Color(161, 209, 82)
blue = pygame.Color(79, 125, 238)

# Initialize Pygame
pygame.init()

# Initialize the game window and set the caption
pygame.display.set_caption("PYTHON - A Snake Game")
game_window = pygame.display.set_mode((720, 480))

# create the frames per second controller with an FPS variable
fps = pygame.time.Clock()

# define the default snake position
snake_position = [100, 50]

# create the first 4 blocks of the snake's body
snake_body = [[100, 50],
                 [90, 50],
                 [80, 50],
                 [70, 50]
                 ]

# set the fruit position to a random spot and give it a boolean switch
fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                  random.randrange(1, (window_y // 10)) * 10]

fruit_spawn = True

# set the default snake position to be moving rightward
direction = "RIGHT"
change_to = direction

# set the initial score to zero
score = 0

# create a function to spawn the fruit
def spawn_fruit():
    global fruit_spawn
    global fruit_position
    fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                  random.randrange(1, (window_y // 10)) * 10]
    fruit_spawn = True

# create a function to draw the snake
def draw_snake():
    game_window.fill(light_green)
    for block in snake_body:
        pygame.draw.rect(blue)
    for fruit in fruit_position:
        pygame.draw.rect(red)

# create a function to check if the game is over
def check_game_over():
    my_font = pygame.font.SysFont("Arial", 50)
    game_over_surface = my_font.render(f"Game Over! Final Score: {score}", True, red)
    game_over_rectangle = game_over_surface.get_rect()
    game_over_rectangle.midtop = window_x/2, window_y/4
    game_window.blit(game_over_surface, game_over_rectangle)
    pygame.display.flip()

    time.sleep(3)
    pygame.quit()
    quit()


# create a function to check if there is a collision

def check_collision():
    global snake_body
    global snake_position
    for block in snake_body[1:]:
        if snake_position == snake_position[0]:
            # game_over()
            pygame.display.set_caption("Game Over Example")

# create a function to show the score

def show_score(choice, color, font, size):
    global score
    global game_window
    global white
    font = pygame.font.SysFont(font, size)
    surface = font.render(f"{score}", True, color)
    score_rectangle = surface.get_rect()
    game_window.blit(surface, score_rectangle)


def main():
    global change_to, direction, fruit_position, score, fruit_spawn

    while True:

        # handling key events
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    change_to = 'UP'
                if event.key == pygame.K_DOWN:
                    change_to = 'DOWN'
                if event.key == pygame.K_LEFT:
                    change_to = 'LEFT'
                if event.key == pygame.K_RIGHT:
                    change_to = 'RIGHT'

        # If two keys pressed simultaneously
        # we don't want snake to move into two
        # directions simultaneously
        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'

        # Moving the snake
        if direction == 'UP':
            snake_position[1] -= 10
        if direction == 'DOWN':
            snake_position[1] += 10
        if direction == 'LEFT':
            snake_position[0] -= 10
        if direction == 'RIGHT':
            snake_position[0] += 10

        # Snake body growing mechanism
        # if fruits and snakes collide then scores
        # will be incremented by 10
        snake_body.insert(0, list(snake_position))
        if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
            score += 10
            fruit_spawn = False
        else:
            snake_body.pop()

        if not fruit_spawn:
            fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                              random.randrange(1, (window_y // 10)) * 10]

        fruit_spawn = True
        game_window.fill(light_green)

        for pos in snake_body:
            pygame.draw.rect(game_window, blue,
                             pygame.Rect(pos[0], pos[1], 10, 10))
        pygame.draw.rect(game_window, red, pygame.Rect(
            fruit_position[0], fruit_position[1], 10, 10))

        if snake_position[0] < 0 or snake_position[0] > window_x-10:
            check_game_over()

        if snake_position[1] < 0 or snake_position[1] > window_y-10:
            check_game_over()

        for block in snake_body[1:]:
            if snake_position[0] == block[0] and snake_position[1] == block[1]:
                check_game_over()

        show_score(1, black, "Arial", 20)
        pygame.display.update()
        fps.tick(speed)

if __name__ == '__main__':
    main()
