import pygame
import link


title_font = pygame.font.Font('assets/Press-Start2P.ttf', 60)
title_text = title_font.render('SnakeEx', True, link.BLACK)
title_rect = title_text.get_rect(center= (240,180))

play_font = pygame.font.Font('assets/Press-Start2P.ttf', 36)
play_text = play_font.render('PLAY', True, link.BLACK)
play_rect = play_text.get_rect(center= (240,260))

quit_font = pygame.font.Font('assets/Press-Start2P.ttf', 36)
quit_text = quit_font.render('QUIT', True, link.BLACK)
quit_rect = quit_text.get_rect(center= (240,320))


def start():
    pass


def update():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            link.quit()

    if pygame.mouse.get_pressed()[0]:
        pos = pygame.mouse.get_pos()
        
        if play_rect.collidepoint(pos):
            link.play('snake')
            link.play('gameover')
        elif quit_rect.collidepoint(pos):
            link.quit()

    link.draw(link.background,(0,0))
    link.draw(title_text, title_rect)
    link.draw(play_text, play_rect)
    link.draw(quit_text, quit_rect)
        
