from .character import *
from ..map import *

class FriendlyBot(Character):
    def __init__(self, x, y, width, height):
        Character.__init__(self, x, y, width, height, "friendly_bot/breath/1.png", 0)
        self.list_breath = self.create_animations_list("friendly_bot/breath", 2)
        
    def animation(self):
        self.play_animation(20, 39, self.list_breath)
    
bot1 = FriendlyBot(1125, 320, 80, 80)
map.enemy_list.append(bot1)
