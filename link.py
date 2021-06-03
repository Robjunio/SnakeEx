import pygame
import sys

# Colors
BLACK = (0, 0, 0)

screen = None
game_clock = pygame.time.Clock()
background = pygame.image.load('assets/snake2-background.png')


def quit():
    pygame.quit()
    exit()

def draw(surface, pos):
    screen.blit(surface, pos)


def play(scene_name):
    global fps
    fps = 10

    scene = sys.modules[scene_name]
    scene.start()
    game = False

    while not game:
        game_clock.tick(fps)
        game = scene.update()
        pygame.display.flip()
