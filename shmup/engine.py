import sys,pygame, ship

pygame.init()
fpsClock = pygame.time.Clock()
size = width, height = 1024, 768
screen = pygame.display.set_mode(size)
hero = ship.Hero()

def paint():
        screen.fill([0, 0, 0])
        screen.blit(hero.draw(), hero.rect)
        pygame.display.flip()
def getInput():
        for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
        keys = pygame.key.get_pressed()
        hero.move(keys, pygame.mouse.get_pos())
        

while 1:
        getInput()
        paint()
        fpsClock.tick(60) 
        



