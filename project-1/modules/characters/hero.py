import pygame
from ..settings import *
from .character import *

class Hero(Character):
    def __init__(self, x, y, height, width, name, speed):
        Character.__init__(self, x, y, height, width, name, speed)
        self.list_run = self.create_animations_list("hero/run", 6)
        self.list_run_left = self.create_animations_list("hero/run", 6, True)
        self.list_jump = self.create_animations_list("hero/jump", 2)
        self.list_jump_left = self.create_animations_list("hero/jump", 2, True)
        self.list_breath = self.create_animations_list("hero/breath", 11)

        self.is_hold_blaster = False
        self.list_shooting_run = self.create_animations_list('hero/shooting_run', 6)
        self.list_shooting_run_left = self.create_animations_list('hero/shooting_run', 6, True)

        self.count_heart = 3
        self.image_heart = Sprite(0, 25, 50, 50, 'heart.png')
        self.empty_image_heart = Sprite(0, 25, 50, 50, 'empty_heart.png')
    
    def show_stats(self):
        for count in range(3):
            if count < self.count_heart:
                screen.blit(self.image_heart.image, (50 * (count + 2), 25))
            else:
                screen.blit(self.empty_image_heart.image, (50 * (count + 2), 25))

    def jump(self):
        if self.list_key[pygame.K_SPACE] and self.can_fall == False:
            # Триггер который говорит, что мы можем прыгать
            # Задаёт резкость прыжка
            self.jump_counter = 23

        if self.jump_counter > 0:
            self.jump_counter -= 1
            # Высота прыжка
            self.y -= 8
            if self.direction == 'right':
                self.image = self.list_jump[0]
            else:
                self.image = self.list_jump_left[0]
    
        
    def move(self):
        # get_pressed - метод который возвращает список клавиш
        # [False, True, False] - где каждое значение - нажата ли клавиша
        # K_a, K_d, K_w ... - сохраняют индексы этого списка

        self.list_key = pygame.key.get_pressed()
        self.check_colision()
        self.jump()    
        
        if self.list_key[pygame.K_d] == True and self.can_move_right:
            self.x = self.x + self.speed
            self.direction = "right"
            if self.is_hold_blaster:
                self.play_animation(5, 29, self.list_shooting_run, self.list_shooting_run_left)
            else:
                self.play_animation(5, 29, self.list_run, self.list_run_left)
                
        elif self.list_key[pygame.K_a] == True and self.can_move_left:
            self.x = self.x - self.speed
            self.direction = "left"
            if self.is_hold_blaster:
                self.play_animation(5, 29, self.list_shooting_run, self.list_shooting_run_left)
            else:
                self.play_animation(5, 29, self.list_run, self.list_run_left)
                
        elif self.jump_counter == 0 and self.can_fall == False:
            self.play_animation(15, 164, self.list_breath)
        if self.can_fall and self.jump_counter == 0:
            self.y += 5
            if self.direction == "right":
                self.image = self.list_jump[1]
            else:
                self.image = self.list_jump_left[1]


main_hero = Hero(200, 0, 80, 80, "hero.png", 5)
