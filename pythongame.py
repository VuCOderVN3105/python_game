import pygame

pygame.init()

screen = pygame.display.set_mode((1080,480))
pygame.display.set_caption('First Game in Pygame')
clock = pygame.time.Clock()
icon = pygame.image.load('C:/Users/Public/Pics/macOS BigSur ICONS by Maiguris/Visual Studio Code Regular.png')
running = True
while running:
    clock.tick(60)
    screen.blit(icon,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
pygame.quit()
