import pygame, sys, Laser
class Battlecruiser(pygame.sprite.Sprite):
        def __init__(self, screen):
                pygame.sprite.Sprite.__init__(self)
                self.screen = screen
                try:
                        self.image = pygame.image.load('assets/battlecruiser.gif').convert()
                except:
                        self.image = pygame.Surface((200, 200))
                self.x = 0;
                self.y = 0;
                self.dx = 0;
                self.dy = 0;
                self.speed = 3
                self.lasers = pygame.sprite.Group()
                (self.image_w, self.image_h) = self.image.get_size()
                self.rect = self.image.get_rect().move(self.x, self.y)
                self.active = True
        def move(self, keys):
                if (keys[pygame.K_UP]):
                        self.dy = -self.speed
                elif (keys[pygame.K_DOWN]):
                        self.dy = self.speed
                else:
                        self.dy = 0
                if (keys[pygame.K_LEFT]):
                        self.dx = -self.speed
                elif (keys[pygame.K_RIGHT]):
                        self.dx = self.speed
                else:
                        self.dx = 0
                if (keys[pygame.K_SPACE]):
                        self.shoot()
        def shoot(self):
                self.lasers.add(Laser.Laser(self.x + (self.image_w/2), self.y, self.screen))
        def update(self):
                self.x += self.dx
                self.y += self.dy
                self.rect.x = self.x
                self.rect.y = self.y
        def draw(self):
                screen.blit(self.image, self.rect)



if __name__ == "__main__":
        pygame.init()
        fpsClock = pygame.time.Clock()
        size = width, height = 800, 600
        screen = pygame.display.set_mode(size)
        battle = Battlecruiser(screen)

        while 1:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT: sys.exit()
                keys = pygame.key.get_pressed()
                if (keys[pygame.K_ESCAPE]):
                        sys.exit()
                screen.fill(16777215)
                battle.move(keys)
                battle.update()
                battle.draw()
                battle.lasers.update()
                battle.lasers.draw(screen)
                pygame.display.flip()

                fpsClock.tick(50)
