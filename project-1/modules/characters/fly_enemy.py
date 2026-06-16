from .character import *
from ..map import *
class FlyEnemy(Character):
    def __init__(self, x, y, width, height, finish_x, speed):
        Character.__init__(self, x, y, width, height, 'enemy1/fly/0.png', speed)
        self.list_fly = self.create_animations_list('enemy1/fly', 2)
        self.list_fly_left = self.create_animations_list('enemy1/fly', 2, True)
        self.finish_x = finish_x
        self.start_x = x

    def fly(self):
        if self.direction == 'right':
            self.x += self.speed
            if self.x >= self.finish_x:
                self.direction = 'left'
        else:
            self.x -= self.speed
            if self.x <= self.start_x:
                self.direction = 'right'
        self.play_animation(15, 29, self.list_fly, self.list_fly_left)
        
    def animation(self):
        self.fly()
    
fly_enemy1 = FlyEnemy(500, 150, 140, 140, 1000, 3)
map.enemy_list.append(fly_enemy1)