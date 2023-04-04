import pygame
import os

pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height),0,32)
Run    = [pygame.image.load(os.path.join("assets/Dino", "DinoRun1.png")),
         pygame.image.load(os.path.join("D:/Projects/Dino-2.O/assets/Dino/DinoRun2.png"))]

Jump  = pygame.image.load(os.path.join("D:/Projects/Dino-2.O/assets/Dino/DinoJump.png"))

Duck = [pygame.image.load(os.path.join("assets/Dino", "DinoDuck1.png" )),
        pygame.image.load(os.path.join("assets/Dino", "DinoDuck2.png"))]

Small_cactus=[pygame.image.load(os.path.join("assets/Cactus", "SmallCactus1.png")),
        pygame.image.load(os.path.join("assets/Cactus", "SmallCactus2.png")),
        pygame.image.load(os.path.join("assets/Cactus", "SmallCactus3.png" )) ]

Large_cactus=[pygame.image.load(os.path.join("assets/Cactus", "LargeCactus1.png")),
        pygame.image.load(os.path.join("D:/Projects/Dino-2.O/assets/Cactus/LargeCactus2.png")),
        pygame.image.load(os.path.join("D:/Projects/Dino-2.O/assets/Cactus/LargeCactus3.png" )) ]

Bird = [pygame.image.load(os.path.join("assets/Bird", "Bird1.png")),
        pygame.image.load(os.path.join("assets/Bird", "Bird2.png"))]

Cloud = [pygame.image.load(os.path.join("assets/Cloud.png"))]

BG= [pygame.image.load(os.path.join("assets/Track.png"))]


class Dino:
    X_pos = 80
    Y_pos = 310
    Y_pos_duck = 340

    def __init__(self):
        self.duck_img = Duck
        self.run_img = Run
        self.jump_img = Jump
        self.dino_duck = False
        self.dino_run = True
        self.dino_jump =False

        self.step_index = 0
        self.image = self.run_img[0]
        self.dino_rect =  self.image.get_rect()
        self.dino_rect.x = self.X_pos
        self.dino_rect.y = self.Y_pos

    def update(self, userInput):
        if self.dino_duck:
            self.duck()
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()
        if self.step_index >= 10:
            self.step_index = 0
        if userInput[pygame. K_UP] and not self.dino_jump:
            self.dino_duck =False
            self.dino_run = False
            self.dino_jump = True
        elif userInput[pygame.K_DOWN] and not self.dino_jump:
            self.dino_duck =True
            self.dino_run = False
            self.dino_jump = False
        elif not (self.dino_jump or userInput[pygame.K_DOWN]):
            self.dino_duck =False
            self.dino_run = True
            self.dino_jump = False

    def duck(self):
        pass

    
    
    def run(self):
        pass

    def jump(self):
        pass
        
    def draw(self, screen):
        screen.blit(self.image,(self.dino_rect.x,self.dino_rect.y))





        pass

def main():
    run  = True
    clock = pygame.time.Clock()
    player = Dino()
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        screen.fill((255,255,255))
        userInput = pygame.key.get_pressed()

        player.draw(screen)
        player.update(userInput)
        clock.tick(30)
        pygame.display.update()

main()
