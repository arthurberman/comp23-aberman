import pygame, random
class Laser(pygame.sprite.Sprite):
        def __init__(self, x, y, screen):
                pygame.mixer.Sound('assets/laser.wav').play()
                pygame.sprite.Sprite.__init__(self)
                self.x = x
                self.y = y
                self.dy = -5
                self.dx = 0
                self.screen = screen
                try:
                        self.image = pygame.image.load('assets/laser.gif').convert()
                except:
                        self.image = pygame.Surface((50, 50))

                (self.image_w, self.image_h) = self.image.get_size()
                self.rect = self.image.get_rect().move(self.x, self.y)
                self.active = True
        def update(self):
                self.x += self.dx
                self.y += self.dy
                self.rect.x = self.x
                self.rect.y = self.y
                if self.rect.y < 0:
                    self.active = False
        def draw(self):
                if self.active:
                    self.screen.blit(self.image, self.rect)
if __name__ == "__main__":
        pygame.init()
        fpsClock = pygame.time.Clock()
        size = width, height = 800, 600
        screen = pygame.display.set_mode(size)
        lasers = pygame.sprite.Group()
        while 1:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT: sys.exit()
                keys = pygame.key.get_pressed()
                if (keys[pygame.K_ESCAPE]):
                        sys.exit()
                if (random.random() * 5  > 3):
                        lasers.add(Laser(random.random() * 800, 600, screen))
                screen.fill(16777215)
                lasers.update()
                lasers.draw(screen)
                pygame.display.flip()

                fpsClock.tick(50)
