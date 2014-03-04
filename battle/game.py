import pygame, sys, Battlecruiser, Enemy, Laser, random
from Battlecruiser import *

if __name__ == "__main__":
        pygame.init()
        fpsClock = pygame.time.Clock()
        size = width, height = 800, 600
        screen = pygame.display.set_mode(size)
        battle = Battlecruiser(screen)
        enemies = pygame.sprite.Group()
        score = 0
        try:
            background = pygame.image.load('assets/ram_aras.png').convert()
        except:
            background = pygame.Surface((200, 200))
        worldY = 0
        gameOver = False
        while not gameOver:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT: sys.exit()

                if random.random() * 100 > 98:
                    enemies.add(Enemy.Enemy(screen, battle, random.random() * 800, - 10))
                keys = pygame.key.get_pressed()
                if (keys[pygame.K_ESCAPE]):
                        sys.exit()
                screen.fill(16777215)
                screen.blit(background, screen.get_rect().move(0, worldY))
                screen.blit(background, screen.get_rect().move(0, worldY-3000))
                worldY += 1
                worldY = worldY % 3000
                battle.move(keys)
                battle.update()
                battle.draw()
                battle.lasers.update()
                enemies.update(False)
                collisions = filter((lambda col: col.rect.colliderect(battle.rect) and col.active), enemies)
                if (len(collisions) > 0):
                        pygame.mixer.Sound('assets/death_explode.wav').play()
                        gameOver = True
                for enemy in enemies:
                    collisions = filter((lambda col: col.rect.colliderect(enemy.rect) and col.active), battle.lasers)
                    if len(collisions) > 0:
                        enemy.hit()
                        score += 100
                        for laser in collisions:
                            laser.active = False
                for laser in battle.lasers:
                    laser.draw()
                for enemy in enemies:
                    enemy.draw()
                scoreText = pygame.font.SysFont(pygame.font.get_default_font(), 100).render(str(score), True, (255, 255, 255))
                screen.blit(scoreText, scoreText.get_rect())
                pygame.display.flip()

                fpsClock.tick(50)



        scoreText = pygame.font.SysFont(pygame.font.get_default_font(), 100).render("Game Over", True, (255, 255, 255))
        screen.blit(scoreText, scoreText.get_rect().move(250, 300))
        pygame.display.flip()
        for x in range(5):
            fpsClock.tick(1)
