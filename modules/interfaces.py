import sys
import pygame


def Button(screen, position, text, cfg):
    bwidth = 310 #set the width of the buttons  
    bheight = 65 #set the height of the buttons
    left, top = position #sets the position of the buttons
    pygame.draw.line(screen, (150, 150, 150), (left, top), (left+bwidth, top), 5)
    pygame.draw.line(screen, (150, 150, 150), (left, top - 2), (left, top + bheight), 5)
    pygame.draw.line(screen, (50, 50, 50), (left, top + bheight), (left + bwidth, top + bheight), 5)
    pygame.draw.line(screen, (50, 50, 50), (left + bwidth, top + bheight), (left + bwidth, top), 5)
    pygame.draw.rect(screen, (100, 100, 100), (left, top, bwidth, bheight))
    font = pygame.font.Font(cfg.FONTPATH, 50)
    text_render = font.render(text, 1, (255, 0, 0))
    return screen.blit(text_render, (left + 50, top + 10))

def StartInterface(screen, cfg):
    clock = pygame.time.Clock()
    while True:
        button_1 = Button(screen, (330, 190), 'SinglePlayer', cfg) #sets the buttons names and assigns it to button_1
        button_2 = Button(screen, (330, 305), 'MultiPlayer', cfg)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_1.collidepoint(pygame.mouse.get_pos()):
                    return 1
                elif button_2.collidepoint(pygame.mouse.get_pos()):
                    return 2
        clock.tick(60)
        pygame.display.update()
        

def EndInterface(screen, cfg):
    clock = pygame.time.Clock()
    while True:
        button_1 = Button(screen, (330, 190), 'Restart', cfg)
        button_2 = Button(screen, (330, 305), 'Exit', cfg)
        button_3 = Button(screen, (300, 305), 'Return to main menu', cfg)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_1.collidepoint(pygame.mouse.get_pos()):
                    return
                elif button_2.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
                    sys.exit()
        clock.tick(60)
        pygame.display.update()
                
        

        
                
                
        
        
        
        
        
        
        
        
        
        
    