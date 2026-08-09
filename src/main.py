import pygame

class Game:
    def __init__(self):
        pygame.init()
        self.load_images()
        self.new_game()

    def load_images(self):
        self.images = {"robot": pygame.image.load("robot.png"), "coin": pygame.image.load("coin.png"), "monster": pygame.image.load("monster.png")}

    def new_game(self):
        self.score = 0
        self.falling_objects = []
        #self.robot = instantiate new robot after Robot class is defined

    def main_loop(self):
        while True:
            self.check_events()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()