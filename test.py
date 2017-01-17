import pygame

display_width=800
display_height=600
pygame.init()
gameDisplay= pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Yung Crysthal Why You Trappin So Hard')
clock=pygame.time.Clock()

died= False

while not died:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            died=True

        print(event)

    pygame.display.update()
    clock.tick(60)

pygame.quit    
