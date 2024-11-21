import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    field = AsteroidField()

    Shot.containers = (updatable, drawable, shots)

    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    return

        screen.fill((0,0,0))

        for u in updatable:
            u.update(dt)

        for a in asteroids:
            if a.check_collision(player):
                print("Game over!")
                return
            
            for s in shots:
                if a.check_collision(s):
                    a.split()
                    s.kill()

        for d in drawable:
            d.draw(screen)

        pygame.display.flip()
        ms = clock.tick(60)
        dt = ms / 1000

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()
