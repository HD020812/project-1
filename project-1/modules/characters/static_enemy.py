from .character import *
from .hero import *
from ..map import *

class StaticEnemy(Character):
    def __init__(self, x, y, height, width, direction):
        Character.__init__(self, x, y, height, width, "enemy2/atack/0.png", 0)
        self.direction = direction

        self.list_atack = self.create_animations_list('enemy2/atack', 6)
        self.list_atack_left = self.create_animations_list('enemy2/atack', 6, True)

    def animation(self):
        if self.image_counter > 0:
            self.play_animation(10, 59, self.list_atack, self.list_atack_left)
        else:
            if self.direction == 'right':
                self.image = self.list_atack[0]
            else:
                self.image = self.list_atack_left[0]

        self.atack()


    
    def atack(self):
        if self.direction == "right":
            enemy_rect = pygame.Rect(self.x + self.width / 2, self.y, self.width * 0.75, self.height)
        else:
            enemy_rect = pygame.Rect(self.x - self.width / 4, self.y, self.width * 0.75, self.height)

        # pygame.draw.rect(screen, "yellow", enemy_rect)

        if main_hero.hero_rect.colliderect(enemy_rect) and self.image_counter == 0:
            self.image_counter = 1
        
        if self.image_counter == 58 and main_hero.hero_rect.colliderect(enemy_rect):
            main_hero.count_heart -= 1


static_enemy1 = StaticEnemy(730, 320, 80, 80, 'left')
map.enemy_list.append(static_enemy1)