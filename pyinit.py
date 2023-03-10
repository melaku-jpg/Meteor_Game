import pygame
import os
width, height = 800, 600 #used to define the width and height of console window

GScreen = pygame.display.set_mode((width, height)) # used for displaying our window 
pygame.display.set_caption("Maze Game") #Used for naming the title of the console
PICTURE = pygame.image.load(os.path.join('resources/images', 'download.png')) #Used for importing pictures from our storage with the help of os
SONG = os.path.join(os.getcwd(), 'resources/sounds/Ferreck Dawn vs. Franky Rizardo ft. Torica - Baby Slow Down (Extended Mix).mp3') #used for importing music
FPS = 144
def draw_fn():
    GScreen.fill((255, 0, 255))
    GScreen.blit(PICTURE, (0,0)) 

    pygame.display.update()

def main():
    run = True
    pygame.mixer.init()
    pygame.mixer.music.load(SONG)
    pygame.mixer.music.play(-1)
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        draw_fn()
if __name__ == "__main__":
    main()