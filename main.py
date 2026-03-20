import pygame

from constants import SCREEN_WIDTH
from constants import SCREEN_HEIGHT
from logger import log_state

BLACK = (0, 0, 0)

def main():
    print("Starting Asteroids with pygame version: (%s)" % pygame.version.ver)
    print("Screen width: 1280")
    print("Screen height: 720")
    pygame.init()
    
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        screen.fill("black")
        pygame.display.flip()

if __name__ == "__main__":
    main()
