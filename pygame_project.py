import pygame
screen = pygame.display.set_mode((1500, 700))
pygame.display.set_caption('project')
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                screen.fill((255, 0, 0))
                pygame.display.flip()  
            if event.key == pygame.K_g:
                screen.fill((0, 255, 0))
                pygame.display.flip()  
            if event.key == pygame.K_b:
                screen.fill((0, 0, 255))
                pygame.display.flip()  
            if event.key == pygame.K_y:
                screen.fill((255, 225, 0))
                pygame.display.flip()  
            if event.key == pygame.K_v:
                screen.fill((225, 0, 255))
                pygame.display.flip()
            if event.key == pygame.K_o:
                screen.fill((255, 75, 0))
                pygame.display.flip() 
            if event.key == pygame.K_c:
                screen.fill((0, 255, 255))
                pygame.display.flip() 
            if event.key == pygame.K_p:
                screen.fill((255, 0, 120))
                pygame.display.flip()
            