import pygame
import PlayerClass, AlienClass

pygame.init()

Width = 1200
Height = 700
display_surface = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Space Invaders")

FPS = 60
clock = pygame.time.Clock()


class Game():


    def __init__(self, player, alien_group, player_bullet_group, alien_bullet_group):

        self.round_number = 1
        self.score = 0

        self.player = player
        self.alien_group = alien_group
        self.player_bullet_group = player_bullet_group
        self.alien_bullet_group = alien_bullet_group


        self.new_round_sound = pygame.mixer.Sound("assets/new_round.wav")
        self.breach_sound = pygame.mixer.Sound("assets/breach.wav")
        self.alien_hit_sound = pygame.mixer.Sound("assets/alien_hit.wav")
        self.player_hit_sound = pygame.mixer.Sound("assets/player_hit.wav")


        self.font = pygame.font.Font("assets/Facon.ttf", 32)


    def update(self):

        self.shift_aliens()
        self.check_collisions()
        self.check_round_completion()


    def draw(self):
        """Draw the HUD and other information to display"""

        WHITE = (255, 255, 255)


        score_text = self.font.render("Score: " + str(self.score), True, WHITE)
        score_rect = score_text.get_rect()
        score_rect.centerx = Width//2
        score_rect.top = 10

        round_text = self.font.render("Round: " + str(self.round_number), True, WHITE)
        round_rect = round_text.get_rect()
        round_rect.topleft = (20, 10)

        lives_text = self.font.render("Lives: " + str(self.player.lives), True, WHITE)
        lives_rect = lives_text.get_rect()
        lives_rect.topright = (Width - 20, 10)


        display_surface.blit(score_text, score_rect)
        display_surface.blit(round_text, round_rect)
        display_surface.blit(lives_text, lives_rect)
        pygame.draw.line(display_surface, WHITE, (0, 50), (Width, 50), 4)
        pygame.draw.line(display_surface, WHITE, (0, Height - 100), (Width, Height - 100), 4)

    def shift_aliens(self):
        """Shift a wave of aliens down the screen and reverse direction"""

        shift = False
        for alien in (self.alien_group.sprites()):
            if alien.rect.left <= 0 or alien.rect.right >= Width:
                shift = True


        if shift:
            breach = False
            for alien in (self.alien_group.sprites()):

                alien.rect.y += 10 * self.round_number


                alien.direction = -1 * alien.direction
                alien.rect.x += alien.direction * alien.velocity


                if alien.rect.bottom >= Height - 100:
                    breach = True


            if breach:
                self.breach_sound.play()
                self.player.lives -= 1
                self.check_game_status("Aliens breached the line!", "Press 'Enter' to continue")

    def check_collisions(self):
        """Check for collisions"""
 
        if pygame.sprite.groupcollide(self.player_bullet_group, self.alien_group, True, True):
            self.alien_hit_sound.play()
            self.score += 100


        if pygame.sprite.spritecollide(self.player, self.alien_bullet_group, True):
            self.player_hit_sound.play()
            self.player.lives -= 1

            self.check_game_status("You've been hit!", "Press 'Enter' to continue")

    def check_round_completion(self):
        """Check to see if a player has completed a single round"""

        if not (self.alien_group):
            self.score += 1000 * self.round_number
            self.round_number += 1

            self.start_new_round()

    def start_new_round(self):
        """Start a new round"""

        for i in range(11): 
            for j in range(5): 
                alien = AlienClass.Alien(64 + i * 64, 120 + j * 64, self.round_number, self.alien_bullet_group)
                self.alien_group.add(alien)

     
        self.new_round_sound.play()
        self.pause_game("Space Invaders Round " + str(self.round_number), "Press 'Enter' to begin")

    def check_game_status(self, main_text, sub_text):
        """Check to see the status of the game and how the player died"""
 
        self.alien_bullet_group.empty()
        self.player_bullet_group.empty()
        self.player.reset()
        for alien in self.alien_group:
            alien.reset()


        if self.player.lives == 0:
            self.reset_game()
        else:
            self.pause_game(main_text, sub_text)

    def pause_game(self, main_text, sub_text):
        """Pauses the game"""
        global running


        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)


        main_text = self.font.render(main_text, True, WHITE)
        main_rect = main_text.get_rect()
        main_rect.center = (Width // 2, Height // 2)


        sub_text = self.font.render(sub_text, True, WHITE)
        sub_rect = sub_text.get_rect()
        sub_rect.center = (Width // 2, Height // 2 + 64)


        display_surface.fill(BLACK)
        display_surface.blit(main_text, main_rect)
        display_surface.blit(sub_text, sub_rect)
        pygame.display.update()


        is_paused = True
        while is_paused:
            for event in pygame.event.get():

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        is_paused = False

                if event.type == pygame.QUIT:
                    is_paused = False
                    running = False

    def reset_game(self):
        """Reset the game"""
        self.pause_game("Final Score: " + str(self.score), "Press 'Enter' to play again")


        self.score = 0
        self.round_number = 1

        self.player.lives = 5


        self.alien_group.empty()
        self.alien_bullet_group.empty()
        self.player_bullet_group.empty()


        self.start_new_round()

myBulletPlayerGroup = pygame.sprite.Group()

my_player_group = pygame.sprite.Group()
my_player = PlayerClass.Player(myBulletPlayerGroup)
my_player_group.add(my_player)

my_alien_group = pygame.sprite.Group()
my_alien_bullet_group = pygame.sprite.Group()

my_game = Game(my_player, my_alien_group, myBulletPlayerGroup, my_alien_bullet_group)
my_game.start_new_round()

'''
for i in range(10):
    alien = AlienClass.Alien(64 + i * 64, 100, 3, my_alien_bullet_group)
    my_alien_group.add(alien)'''


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                my_player.fire()


    display_surface.fill((0, 0, 0))

    my_player_group.update()
    my_player_group.draw(display_surface)

    myBulletPlayerGroup.update()
    myBulletPlayerGroup.draw(display_surface)

    my_alien_group.update()
    my_alien_group.draw(display_surface)

    my_game.update()
    my_game.draw()

    my_alien_bullet_group.update()
    my_alien_bullet_group.draw(display_surface)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
