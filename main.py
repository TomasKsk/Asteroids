import pygame
import constants as const
from player import Player

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {const.SCREEN_WIDTH}")
    print(f"Screen height: {const.SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((const.SCREEN_WIDTH, const.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    player = Player(const.x, const.y, const.PLAYER_RADIUS)
    dt = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatable.update(dt)
        
        screen.fill("black")
        # player.draw(screen)
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()