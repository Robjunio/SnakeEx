import pygame
from random import randint


pygame.init()


def apple_pos():
    x = randint(0, 480)
    y = randint(0, 480)
    pos_x, pos_y = x - x%20, y - y%20
    return pos_x, pos_y



def collision(pos0, pos1):
    return pos0[0] == pos1[0] and pos0[1] == pos1[1]


# Definindo direções
UP = 0
RIGHT = 1
LEFT = 2
DOWN = 3

background = pygame.image.load('assets/snake2-background.png')

# Creating screen
size = (480, 480)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Snake2')

# Creating snake
snake = [(200, 200), (220,200), (240, 200)]
snake_head = pygame.image.load('assets/snake2_head.png')
snake_head_direction = [snake_head,
                        pygame.transform.rotate(snake_head, -90),
                        pygame.transform.rotate(snake_head, 90),
                        pygame.transform.rotate(snake_head, 180)]
snake_body = pygame.image.load('assets/snake2_body.png')
snake_body_direction = [snake_body,
                        pygame.transform.rotate(snake_body, 90)]
direction = UP

# Creating apple
apple_spawn = apple_pos()
apple = pygame.image.load('assets/snake2-apple.png')
score = 0

ball = pygame.image.load('assets/snake2-balls.png')
ball_dx = 10
ball_dy = 10
ball_x = 40
ball_y = 0

game_loop = True
game_clock = pygame.time.Clock()
fps = 8

while(game_loop):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != DOWN:
                direction = UP
            if event.key == pygame.K_DOWN and direction != UP:
                direction = DOWN
            if event.key == pygame.K_LEFT and direction != RIGHT:
                direction = LEFT
            if event.key == pygame.K_RIGHT and direction != LEFT:
                direction = RIGHT

    if collision(snake[0], apple_spawn):
        score += 1
        apple_spawn = apple_pos()
        snake.append((0,0))

    for i in range(1, len(snake)):
        if collision(snake[0], snake[i]):
            game_loop = False
            
    for i in range(len(snake)):
        if ball_x + 20 >= snake[i][0] >= ball_x:
            if ball_y + 20 >= snake[i][1] >= ball_y:
                game_loop = False

        
    if snake[0][0] + 20 > 480:
        game_loop = False
    elif snake[0][1] + 20 > 480:
        game_loop = False
    elif snake[0][0] < 0:
        game_loop = False
    elif snake[0][1] < 0:
        game_loop = False

    if ball_x +20 > 480:
        ball_dx *= -1
        if score % 2!= 0:
            ball_dy *= -1
    if ball_y + 20 > 480:
        ball_dy *= -1
        if score % 2!= 0:
            ball_dx *= -1
    if ball_y < 0:
        ball_dy *= -1
        if score % 2!= 0:
            ball_dx *= -1
    if ball_x < 0:
        ball_dx *= -1
        if score % 2!= 0:
            ball_dy *= -1
    for i in range(len(snake) - 1, 0, -1):
        snake[i] = snake[i - 1]

    # ball movement
    ball_y += ball_dy
    ball_x += ball_dx
    pos_ball = (ball_x, ball_y)
            
    if direction == UP:
        snake[0] = snake[0][0], snake[0][1] - 20
    if direction == DOWN:
        snake[0] = snake[0][0], snake[0][1] + 20
    if direction == RIGHT:
        snake[0] = snake[0][0] + 20, snake[0][1]
    if direction == LEFT:
        snake[0] = snake[0][0] - 20, snake[0][1]
        
    screen.blit(background, (0, 0))
    screen.blit(ball, (ball_x, ball_y))
    screen.blit(apple, apple_spawn)
    screen.blit(snake_head_direction[direction], snake[0])

    for i in range(1, len(snake)):
        
        if snake[i - 1][0] != snake[i][0]:
            screen.blit(snake_body_direction[1], snake[i])
        else:
            screen.blit(snake_body_direction[0], snake[i])

    game_clock.tick(fps)
    pygame.display.flip()
    
pygame.quit()
