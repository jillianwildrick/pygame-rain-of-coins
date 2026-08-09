import pygame

class Game:
    def __init__(self):
        pygame.init()
        self.load_images()


    def load_images(self):
        self.images = {"robot": pygame.image.load("robot.png"), "coin": pygame.image.load("coin.png"), "monster": pygame.image.load("monster.png")}