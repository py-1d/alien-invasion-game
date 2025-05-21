import pygame, random
Width = 1200
Height = 700

class Alien(pygame.sprite.Sprite):

    def __init__(self, x, y, velocity, bullet_group):
        super().__init__()
        self.image = pygame.image.load("assets/alien.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.starting_x = x
        self.starting_y = y

        self.direction = 1
        self.velocity = velocity
        self.bullet_group = bullet_group

        self.shoot_sound = pygame.mixer.Sound("assets/alien_fire.wav")

    def update(self):

        self.rect.x += self.direction * self.velocity

        if random.randint(0, 1000) > 999 and \
                len(self.bullet_group) < 3:
            self.shoot_sound.play()
            self.fire()

    def fire(self):
        """Fire a bullet"""
        AlienBullet(self.rect.centerx, self.rect.bottom,
                    self.bullet_group)

    def reset(self):
        """Reset the alien position"""
        self.rect.topleft = (self.starting_x, self.starting_y)
        self.direction = 1


class AlienBullet(pygame.sprite.Sprite):
  
    def __init__(self, x, y, bullet_group):
        super().__init__()
        self.image = pygame.image.load("assets/red_laser.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

        self.velocity = 10
        bullet_group.add(self)

    def update(self):
        self.rect.y += self.velocity
     
        if self.rect.top > Height:
            self.kill()

