import pygame

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480

class Game:
    def __init__(self):
        pygame.init()
        self.load_images()
        self.new_game()
        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.game_font = pygame.font.SysFont("Arial", 24)
        self.main_loop()

    def load_images(self):
        self.images = {"robot": pygame.image.load("robot.png"), "coin": pygame.image.load("coin.png"), "monster": pygame.image.load("monster.png")}

    def new_game(self):
        self.score = 0
        self.falling_objects = []
        #self.robot = instantiate new robot after Robot class is defined

    def main_loop(self):
        while True:
            self.check_events()

            self.draw_window()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

    def draw_window(self):
        self.window.fill((0, 0, 0))

        pygame.display.flip()






if __name__ == "__main__":
    Game()