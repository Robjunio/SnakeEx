import pygame
import link


title_font = pygame.font.Font('assets/Press-Start2P.ttf', 40)
title_text = title_font.render('GAMEOVER', True, link.BLACK)
title_rect = title_text.get_rect(center= (240,120))

quit_font = pygame.font.Font('assets/Press-Start2P.ttf', 40)
quit_text = quit_font.render('QUIT', True, link.BLACK)
quit_rect = quit_text.get_rect(center= (240,360))

retry_font = pygame.font.Font('assets/Press-Start2P.ttf', 40)
retry_text = retry_font.render('RETRY', True, link.BLACK)
retry_rect = retry_text.get_rect(center= (240,300))

    
def start():
    pass


def update():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
    if pygame.mouse.get_pressed()[0]:
        pos = pygame.mouse.get_pos()

        if retry_rect.collidepoint(pos):
            link.play('snake')
            
        elif quit_rect.collidepoint(pos):
            link.quit()

    link.draw(link.background, (0,0))
    link.draw(title_text, title_rect)
    link.draw(retry_text, retry_rect)
    link.draw(quit_text, quit_rect)
