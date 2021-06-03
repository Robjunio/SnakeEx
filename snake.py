import pygame
from random import randint
import link

pygame.init()


def collision(pos0, pos1):
    return pos0[0] == pos1[0] and pos0[1] == pos1[1]


def spawn():
    x = randint(0, 480)
    y = randint(0, 480)
    pos_x, pos_y = x - x%20, y - y%20
    pos = (pos_x, pos_y)
    if collision(pos, snake[0]):
        spawn()
    else:
        return pos_x, pos_y


# Directions
U = 0  # Up
R = 1  # Right
L = 2  # Left
D = 3  # Down

snake = [(200, 200), (220,200), (240, 200)]
snake_head = pygame.image.load('assets/snake2_head.png')
snake_head_direction = [snake_head,
                        pygame.transform.rotate(snake_head, -90),
                        pygame.transform.rotate(snake_head, 90),
                        pygame.transform.rotate(snake_head, 180)]
snake_body = pygame.image.load('assets/snake2_body.png')
snake_body_direction = [snake_body,
                        pygame.transform.rotate(snake_body, 90)]
direction = U

apple_pos = spawn()
apple = pygame.image.load('assets/snake2-apple.png')

ball = pygame.image.load('assets/snake2-balls.png')
ball_x = 40
ball_y = 0
ball_dy = 10
ball_dx = 10


def start():
    global snake, apple_pos, direction, ball_y,\
           ball_x, ball_dx, ball_dy
    direction = U
    snake = [(200, 200), (220,200), (240, 200)]
    apple_pos = spawn()
    link.fps = 8
    ball_x = 40
    ball_y = randint(0,480)
    ball_dy = 10
    ball_dx = 10

def update():
    global snake, apple_pos, direction, ball_y,\
           ball_x, ball_dx, ball_dy
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = True
    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != D:
                direction = U
            if event.key == pygame.K_DOWN and direction != U:
                direction = D
            if event.key == pygame.K_LEFT and direction != R:
                direction = L
            if event.key == pygame.K_RIGHT and direction != L:
                direction = R
                
    if collision(snake[0], apple_pos):
        apple_pos = spawn()
        snake.append((0,0))
        
    for i in range(1, len(snake)):
        if collision(snake[0], snake[i]):
            return True
                
    for i in range(len(snake)):
        if ball_x + 20 >= snake[i][0] >= ball_x:
            if ball_y+ 20 >= snake[i][1] >= ball_y:
                 return True
                

    if snake[0][0] + 20 > 480:
        return True
    elif snake[0][1] + 20 > 480:
        return True
    elif snake[0][0] < 0:
        return True
    elif snake[0][1] < 0:
        return True

    random_direct = randint(1,2)   
    if ball_x + 20 > 480:
        ball_dx *= -1
        if random_direct == 2:
            ball_dy *= -1
    if ball_y + 20 > 480:
        ball_dy *= -1
        if random_direct == 2:
           ball_dx *= -1
    if ball_y < 0:
        ball_dy *= -1
        if random_direct == 2:
            ball_dx *= -1
    if ball_x < 0:
        ball_dx *= -1
        if random_direct == 2:
            ball_dy *= -1
            
    for i in range(len(snake) - 1, 0, -1):
        snake[i] = snake[i - 1]

    # ball movement
    ball_y += ball_dy
    ball_x += ball_dx
    pos_ball = (ball_x, ball_y)
            
    if direction == U:
        snake[0] = snake[0][0], snake[0][1] - 20
    if direction == D:
        snake[0] = snake[0][0], snake[0][1] + 20
    if direction == R:
        snake[0] = snake[0][0] + 20, snake[0][1]
    if direction == L:
        snake[0] = snake[0][0] - 20, snake[0][1]
        
    link.draw(link.background, (0, 0))
    link.draw(ball, (ball_x, ball_y))
    link.draw(apple, apple_pos)
    link.draw(snake_head_direction[direction], snake[0])

    for i in range(1, len(snake)):
        if snake[i - 1][0] != snake[i][0]:
            link.draw(snake_body_direction[1], snake[i])
        else:
            link.draw(snake_body_direction[0], snake[i])
