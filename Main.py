import pygame

pygame.init()

import link
import menu
import snake
import gameover


link.screen = pygame.display.set_mode((480, 480))
pygame.display.set_caption('SnakeEx')

link.play('menu')

pygame.quit()
