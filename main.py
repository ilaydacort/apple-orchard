import pygame 
import sys
import random

pygame.init()
font = pygame.font.SysFont(None, 72)

width=800
height=600
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("")


player_img = pygame.image.load("resimler/player.png").convert_alpha()
enemy_img = pygame.image.load("resimler/enemy.png").convert_alpha()
background_img = pygame.image.load("resimler/background.png").convert_alpha()

player_img = pygame.transform.scale(player_img, (80, 70))
enemy_img = pygame.transform.scale(enemy_img, (65, 55))
background_img = pygame.transform.scale(background_img, (width, height))


white=(255,255,255)
purple=(128,0,128)

player_size=50
player_x=width//2
player_y=height//2
speed=5
enemy_size = 50
enemy_x = random.randint(0,750)
enemy_y = random.randint(0,550)
score = 0

clock=pygame.time.Clock()

enemy_speed = 3
difficulty_timer = 0
running=True
game_over = False

while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r and game_over:
                 game_over = False
                 score = 0
                 
                 enemy_speed = 3
                 difficulty_timer = 0

                 player_x = 100
                 player_y = 100
                 enemy_x = random.randint(0,750)
                 enemy_y = random.randint(0,550)

    difficulty_timer += 1
    if difficulty_timer % 300 == 0:
     enemy_speed += 1
    
    if not game_over:
     score += 1
     keys=pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
            current_speed=10
    else:
            current_speed=5

    if keys[pygame.K_LEFT]:
        player_x -= current_speed
    if keys[pygame.K_RIGHT]:
        player_x += current_speed
    if keys[pygame.K_UP]:
        player_y -= current_speed
    if keys[pygame.K_DOWN]:
        player_y += current_speed

    enemy_y += enemy_speed
    if enemy_y > height:
        enemy_y = 0
        enemy_x = random.randint(0, width - enemy_size)

    if player_x<0:
        player_x=0
    if player_x>width-player_size:
        player_x=width-player_size
    if player_y<0:
        player_y=0
    if player_y>height-player_size:
        player_y=height-player_size
        
    player_size = 70
    player_rect = pygame.Rect(player_x + 10, player_y + 10, player_size - 20, player_size - 20)
    enemy_rect = pygame.Rect(enemy_x +5 , enemy_y + 5, enemy_size - 10 , enemy_size - 10)
    

    if player_rect.colliderect(enemy_rect):
     game_over=True
     
    screen.blit(background_img, (0, 0))
    screen.blit(player_img, (player_x, player_y))
    screen.blit(enemy_img, (enemy_x, enemy_y))
    score_text = font.render("Score: " + str(score // 60), True, (0, 0, 0))
    screen.blit(score_text, (20, 20))

    if game_over:
        text = font.render("GAME OVER", True, (255, 0, 0))
        screen.blit(text, (width//2 - 150, height//2 - 50))
    pygame.display.update()


pygame.quit()
sys.exit()

