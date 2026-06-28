from .start import * 

difficulty = "normal"

easy_rect = pygame.Rect(450, 150, 600, 120)
easy_text = font.render("Easy", True, (0, 255, 0))

normal_rect = pygame.Rect(450, 310, 600, 120)
normal_text = font.render("   Normal", True, (255, 200, 0))

hard_rect = pygame.Rect(450, 470, 600, 120)
hard_text = font.render("   Hard", True, (255, 0, 0))


def open_menu():

    menu_bg = Sprite(0, 0, 1500, 700, "menu.png")
    
    close_button = Sprite(20, 20, 50 , 50, "close.png")
    close_rect = pygame.Rect(20, 20, 50 , 50)

    start_rect = pygame.Rect(885, 390, 515, 115)
    exit_rect = pygame.Rect(885, 526, 354, 115)
    settings_rect = pygame.Rect(1268, 526, 123, 115)

    settings_screen = False

    run = True 
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if settings_screen == False:
                    # print(event.pos)
                    # event.pos - переменная которая хранит координаты нажатия на экран
                    # collidepoint - метод который проверяет соприкосновение с определённой точкой
                    if exit_rect.collidepoint(event.pos):
                        run = False
                    if start_rect.collidepoint(event.pos):
                        return start_game(difficulty)
                    
                    if settings_rect.collidepoint(event.pos):
                        settings_screen = True
                else:
                    if close_rect.collidepoint(event.pos):
                        settings_screen = False

                    if easy_rect.collidepoint(event.pos):
                        difficulty = "easy"
                        settings_screen = False

                    if normal_rect.collidepoint(event.pos):
                        difficulty = "normal"
                        settings_screen = False

                    if hard_rect.collidepoint(event.pos):
                        difficulty = "hard"
                        settings_screen = False
                

        menu_bg.show_image()
        
        if settings_screen:
            screen.fill((0, 0, 0))
            close_button.show_image()

            pygame.draw.rect(screen, "green", easy_rect, 5, 10)
            pygame.draw.rect(screen, "yellow", normal_rect, 5, 10)
            pygame.draw.rect(screen, "red", hard_rect, 5, 10)

            screen.blit(easy_text, (650, 170))
            screen.blit(normal_text, (560, 330))
            screen.blit(hard_text, (600, 490))
            
            

        pygame.display.flip()