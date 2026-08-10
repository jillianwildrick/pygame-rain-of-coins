import pygame

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480

class Robot:
    def __init__(self, x: int, y: int, image: pygame.surface):
        self.rect = image.get_rect()
        self.rect.topleft = (x, y)
        self.image = image
        self.to_right = False
        self.to_left = False

    def move(self, width: int):
        if self.to_left:
            self.rect.x -= 3
        if self.to_right:
            self.rect.x += 3
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > width - self.image.get_width():
            self.rect.x = width - self.image.get_width()

    

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