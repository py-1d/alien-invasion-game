import pygame
Width = 1200
Height = 700


class Player(pygame.sprite.Sprite):
    def __init__(self, bullet_group):
        super().__init__()
        self.image = pygame.image.load('assets/player_ship.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = Width//2
        self.rect.bottom = Height

        self.lives = 5
        self.velocity = 8
        self.bulletGroup = bullet_group

        self.shoot_sound = pygame.mixer.Sound("assets/player_fire.wav")

    def update(self):

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.velocity
        if keys[pygame.K_RIGHT] and self.rect.right < Width:
            self.rect.x += self.velocity

    def fire(self):

        if len(self.bulletGroup) < 3:
            PlayerBullet(self.rect.centerx, self.rect.centery, self.bulletGroup)
            self.shoot_sound.play()

    def reset(self):
        self.rect.centerx = Width//2


class PlayerBullet(pygame.sprite.Sprite):

    def __init__(self, x, y, bullet_group):
        super().__init__()
        self.image = pygame.image.load("assets\green_laser.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

        self.velocity = 10
        bullet_group.add(self)

    def update(self):

        self.rect.y -= self.velocity
        if self.rect.bottom < 0:
            self.kill()