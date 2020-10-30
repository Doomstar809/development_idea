import pygame, sys
#Start pygame with .init()
pygame.init()
#creating a display surface. always have a tuple/list with (width, height) of the screen.
screen = pygame.display.set_mode((300,500))
#Frame per second: How many pictures are draw every second. inlfuence how fast a game runs.
clock = pygame.time.Clock()

#importing image: background surface
bg_surface = pygame.image.load("assets/background-day.png").convert()
#scaling surface of images:
#bg_surface = pygame.transform.scale2x(bg_surface)
floor_surface = pygame.image.load("assets/base.png").convert()
#creating game:
while True:
    #checks for events that are happening. ex: clicking something in the game.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
# needs two arguments (surface on the screen surface, locations(x,y))
    screen.blit(bg_surface, (0,0))
    screen.blit(floor_surface, (0,0))
    #takes everything inside the while loop and draws it on the screen.
    pygame.display.update()
    clock.tick(120)