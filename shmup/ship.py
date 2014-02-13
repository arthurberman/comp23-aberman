import pygame, math

class Ship:
        def __init__(self):
                self.x=320
                self.y=240
                self.speed = 7
                self.rect = pygame.Rect(320, 240, 50, 50)
                self.angle = 0
                try:
                        self.image = pygame.image.load('ship.png').convert()
                except:
                        self.image = pygame.Surface(( 50, 50))
        def draw(self):
                surf = pygame.Surface((self.rect.width, self.rect.height))
                surf.blit(self.image, pygame.Rect(0, 0, 50, 50))
                surf2 = pygame.transform.rotate(surf, self.angle)
                return surf2
        def move(self, keys, mouse):
                pass
class Hero(Ship):
        def move(self, keys, mouse):
                mVector = [0, 0]
                if (keys[pygame.K_d]):
                        mVector[0] = 1
                if (keys[pygame.K_a]):
                        mVector[0] = -1
                if (keys[pygame.K_w]):
                        mVector[1] = -1
                if (keys[pygame.K_s]):
                        mVector[1] = 1
                length = math.sqrt((mVector[0] ** 2) + (mVector[1] **2))
                if (length != 0):
                        self.rect.x+=(mVector[0] / length) * self.speed
                        self.rect.y+=(mVector[1] / length) * self.speed
                self.angle = -math.degrees(math.atan2((self.rect.y - mouse[1]), 
                        self.rect.x - mouse[0]))

