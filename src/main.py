import pygame, random

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
        MOVE_RATE = 2
        if self.to_left:
            self.rect.x -= MOVE_RATE
        if self.to_right:
            self.rect.x += MOVE_RATE
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > width - self.image.get_width():
            self.rect.x = width - self.image.get_width()

class FallingObject:
    def __init__(self, x: int, y: int, image: pygame.surface, obj_type: str):
        self.rect = image.get_rect()
        self.rect.topleft = (x, y)
        self.image = image
        self.obj_type = obj_type

    def fall(self):
        FALL_RATE = 1        
        self.rect.y += FALL_RATE
    

class Game:
    def __init__(self):
        pygame.init()
        self.load_images()
        self.new_game()
        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        self.game_font = pygame.font.SysFont("Arial", 24)
        self.main_loop()    

    def load_images(self):
        self.images = {"robot": pygame.image.load("robot.png"), "coin": pygame.image.load("coin.png"), "monster": pygame.image.load("monster.png")}

    def new_game(self):
        self.score = 0
        self.falling_objects = []
        self.robot = Robot(WINDOW_WIDTH//2, WINDOW_HEIGHT - self.images["robot"].get_height(), self.images["robot"])

    def main_loop(self):
        SPAWN_CHANCE = 0.005
        while True:
            self.check_events()
            self.robot.move(WINDOW_WIDTH)
            for obj in self.falling_objects:
                obj.fall()
            if random.random() < SPAWN_CHANCE:
                self.spawn_falling_object()
            for obj in self.falling_objects[:]:
                if self.intercepted(obj):
                    if obj.obj_type == "coin":
                        self.score += 1 
                        self.falling_objects.remove(obj)
                    else:
                        #You lose!
                        return

            self.falling_objects = [obj for obj in self.falling_objects if not self.is_off_screen(obj)]
            self.draw_window()
            self.clock.tick(60)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.robot.to_left = True
                if event.key == pygame.K_RIGHT:
                    self.robot.to_right = True
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.robot.to_left = False
                if event.key == pygame.K_RIGHT:
                    self.robot.to_right = False

    def draw_window(self):
        self.window.fill((0, 150, 255))
        self.window.blit(self.robot.image, self.robot.rect)
        for obj in self.falling_objects:
            self.window.blit(obj.image, obj.rect)
        score_text = self.game_font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.window.blit(score_text, (WINDOW_WIDTH - 150, 10))
        pygame.display.flip()

    def spawn_falling_object(self):
        obj_type = random.choices(["coin", "monster"], weights=[30, 70])[0]
        x = random.randint(0, WINDOW_WIDTH - self.images[obj_type].get_width())
        y = -self.images[obj_type].get_height()
        self.falling_objects.append(FallingObject(x, y, self.images[obj_type], obj_type))

    def is_off_screen(self, obj: FallingObject):
        return obj.rect.y > WINDOW_HEIGHT

    def intercepted(self, obj: FallingObject):
        return self.robot.rect.colliderect(obj.rect)


if __name__ == "__main__":
    Game()