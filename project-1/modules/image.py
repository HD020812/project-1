import os, pygame
from .settings import screen
class Sprite():
    def __init__(self, x, y, height, width, name):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.name = name
        self.image = self.load_image(self.name)
        
    def load_image(self, image_name, flip_x = False):
        path = os.path.join(__file__, "..", "..", "images", image_name)
        path = os.path.abspath(path)
        
        image = pygame.image.load(path)
        
        image = pygame.transform.scale(image, (self.width, self.height))
        if flip_x:
            # pygame.transform.flip - позволяет отзеркалить картинку по нужной оси
            image = pygame.transform.flip(image, True, False,)
        return image

    def show_image(self):
        screen.blit(self.image, (self.x, self.y))
        
    def create_animations_list(self, folder_name, count_image, flip = False):
        list_image = []
        for count in range(count_image):
            image = self.load_image(f'{folder_name}/{count}.png',flip)
            list_image.append(image)
        return list_image
        
background = Sprite(0, 0, 700, 1500, 'bg.png')
    