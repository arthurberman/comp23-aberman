import pygame, sys, random

class Enemy(pygame.sprite.Sprite):
        def __init__(self, screen, player, x, y):
                pygame.sprite.Sprite.__init__(self)
                self.x = x
                self.y = y
                self.dx = 1
                self.dy = 4
                self.screen = screen
                try:
                        self.aliveImage = pygame.image.load('assets/mutalisk.gif')
                        self.explosionImage = pygame.image.load('assets/laser_explosion.gif')
                except:
                        self.aliveImage = pygame.Surface((200, 200))
                        self.explosionImage = pygame.Surface((200, 200))
                self.image = self.aliveImage
                (self.image_w, self.image_h) = self.image.get_size()
                self.rect = self.image.get_rect().move(self.x, self.y)
                self.active= True
                self.thePlayer = player
        def update(self):
                self.x += self.dx
                self.y += self.dy
                if (self.x < 0):
                        self.dx = -self.dx
                if (self.y < 0):
                        self.dy = -self.dy
                if (self.x > 800 -self.image_w):
                        self.dx = -self.dx
                if (self.y > 600 - self.image_h):
                        self.dy = -self.dy
                self.rect.x = self.x
                self.rect.y = self.y
        def draw(self):
                screen.blit(self.image, self.rect)

if __name__ == "__main__":
        pygame.init()
        fpsClock = pygame.time.Clock()
        size = width, height = 800, 600
        screen = pygame.display.set_mode(size)
        enemies = pygame.sprite.Group()
        for x in range(10):
                enemies.add(Enemy(screen, None, random.random() * 800, random.random() * 600))
        while 1:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT: sys.exit()
                keys = pygame.key.get_pressed()
                if (keys[pygame.K_ESCAPE]):
                        sys.exit()
                screen.fill(16777215)
                enemies.update()
                enemies.draw(screen)
                pygame.display.flip()

                fpsClock.tick(50)
