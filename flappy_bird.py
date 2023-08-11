# create by Exin (:
#telegram : @Exin_mood

import pygame
import sys
import random


pygame.init()

#------------ FUNCTION ------------

def generate_pipe_rect():
    random_pipe = random.randrange(130, 500)
    pipe_rect_up = my_pipe.get_rect(midbottom=(700, random_pipe - 183))
    pipe_rect_down = my_pipe.get_rect(midtop=(700, random_pipe))
    return pipe_rect_down,pipe_rect_up

def move_pipe_rect(pipes):
    for pipe in pipes :
        pipe.centerx -= 4
    inside_pipe = [pipe for pipe in pipes if pipe.right > -50]
    return inside_pipe
                                 
def display_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= 650:
            my_screen.blit(my_pipe, pipe)
        else :
            reverse_pipe = pygame.transform.flip(my_pipe,False,True)
            my_screen.blit(reverse_pipe, pipe)

def check_collision(pipes):
    global score , active_score
    for pipe in pipes :
        if bird_image_rect.colliderect(pipe):
            my_sound_2.play()
            active_score = True
            score = 0 
            return False
        if bird_image_rect.top <= -40 or bird_image_rect.bottom >= 530 :
            my_sound_2.play()
            active_score = True
            score = 0 
            return False
    return True

def animation():
    new_bird = bird_list[bird_list_index]
    new_bird_rect = new_bird.get_rect(center=(70, bird_image_rect.centery))
    return new_bird, new_bird_rect

def quit_game():
    e = exit()
    return e
    
def the_score(status):
    global score , high_score 
    if status == "ACTIVE":
        text_1 = game_font.render(str(score),False,(255,255,255))
        text_rect = text_1.get_rect(center=(197.5, 20))
        my_screen.blit(text_1 , text_rect)
    
    if status == "GAME OVER":
             
        text_1 = game_font_2.render(format('FLAPPY BIRD'),False,(254, 254, 1))
        text_rect = text_1.get_rect(center=(197.5, 90))
        my_screen.blit(text_1 , text_rect)
            
        #text_1 = game_font.render(str(score),True,(255,255,255))
        #text_rect = text_1.get_rect(center=(197, 200))
        #my_screen.blit(text_1 , text_rect)
        
        text_2 = game_font.render(str(high_score),True,(255,255,255))
        text_rect = text_2.get_rect(center=(197, 190))
        my_screen.blit(text_2 , text_rect)

        text_1 = game_font.render(format('play : F'),False,(255,255,255))
        text_rect = text_1.get_rect(center=(197, 230))
        my_screen.blit(text_1 , text_rect)

        text_1 = game_font.render(format('flap : space'),False,(255,255,255))
        text_rect = text_1.get_rect(center=(197, 270))
        my_screen.blit(text_1 , text_rect)

        #text_1 = game_font.render(format('----------- HELP -----------'),False,(255, 0, 0))
        #text_rect = text_1.get_rect(center=(197, 360))
        #my_screen.blit(text_1 , text_rect)

        text_1 = game_font.render(format('double flap : up'),False,(255,255,255))
        text_rect = text_1.get_rect(center=(197, 310))
        my_screen.blit(text_1 , text_rect)

        text_1 = game_font.render(format('music : Y'),False,(255,255,255))
        text_rect = text_1.get_rect(center=(197, 350))
        my_screen.blit(text_1 , text_rect)

        #text_1 = game_font_3.render(format('Exin'),False,(0, 84, 240))
        #text_rect = text_1.get_rect(center=(40, 625))
        #my_screen.blit(text_1 , text_rect)

        text_1 = game_font.render(format('stop music : U'),False,(255,255,255))
        text_rect = text_1.get_rect(center=(197, 390))
        my_screen.blit(text_1 , text_rect)

        text_1 = game_font.render(format('exit : Q'),False,(255,255,255))
        text_rect = text_1.get_rect(center=(197, 430))
        my_screen.blit(text_1 , text_rect)
        
def update_score():
    global score, high_score, active_score
    if pipe_list:
        for pipe in pipe_list:
            if 65 < pipe.centerx < 75 and active_score:
                snd()
                score += 1
                active_score = False
                return score 
            if pipe.centerx == 0:
                active_score = True
    if score > high_score :
        high_score = score
                 
    return high_score

def snd():
    global my_sound
    my_sound.play()
    return my_sound

#------------ IMAGE'S ------------

my_screen = pygame.display.set_mode((395, 650))
my_back = pygame.transform.scale2x(pygame.image.load('images/back7.png'))
my_floor = pygame.transform.scale2x(pygame.image.load('images/floor.png'))
my_title = pygame.display.set_caption('Flappy Bird (Night)')
my_pipe = pygame.transform.scale2x(pygame.image.load('images/pipe_green.png'))

my_bird_up = pygame.transform.scale2x(pygame.image.load('images/upp.png'))
my_bird_mid = pygame.transform.scale2x(pygame.image.load('images/mid.png'))
my_bird_down = pygame.transform.scale2x(pygame.image.load('images/down.png'))

#------------ VAREABLE ------------

time_game = pygame.time.Clock()
floor_column = 0
gravity = 0.25
bird_movment = 0

game_status = False
pipe_list = []
bird_list_index = 1
bird_list = [my_bird_up , my_bird_up , my_bird_mid , my_bird_down]
my_bird = bird_list[bird_list_index]

score = 0
high_score = 0
active_score = True

#------------ USEREVENT'S ------------

create_pipe = pygame.USEREVENT
create_flap = pygame.USEREVENT + 1
pygame.time.set_timer(create_flap, 404)
pygame.time.set_timer(create_pipe, 1300)

#------------ SOUND ------------

my_sound = pygame.mixer.Sound('sound/smb_stomp.wav')
my_sound_2 = pygame.mixer.Sound('sound/effect999.mp3')
my_sound_3 = pygame.mixer.Sound('sound/music_up.mp3')
my_sound_4 = pygame.mixer.Sound('sound/Khanjar.mp3')

#------------ FONT ------------

game_font = pygame.font.Font('Font/Pixeled.ttf', 15)
game_font_2 = pygame.font.Font('Font/Pixeled.ttf', 35)
game_font_3 = pygame.font.Font('Font/classic.otf', 22)

#------------ VIRTUAL RECT ------------

bird_image_rect = my_bird.get_rect(center=(70, 300))

#------------ LOOP FOR EVENTS ------------
while True:
    for event in pygame.event.get():   
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_movment = 0
                bird_movment -= 6
            if event.key == pygame.K_UP:
                bird_movment = 0
                bird_movment -= 8
            if event.key == pygame.K_q:
                quit_game()
            if event.key == pygame.K_y:
                my_sound_4.play()
            if event.key == pygame.K_u:
                my_sound_4.stop()
            if event.key == pygame.K_f and game_status == False :
                game_status = True
                pipe_list.clear()
                bird_image_rect.center =(70,300)
                bird_movment = 0
        
        if event.type == create_pipe:
            pipe_list.extend(generate_pipe_rect())
            
            
        if event.type == create_flap:            
            if bird_list_index <= 2:
                bird_list_index += 1
                
            else :
                bird_list_index = 0
            new_bird, new_bird_rect = animation()
                   
    my_screen.blit(my_back , (0, 0))
    if game_status:
        game_status = check_collision(pipe_list)
        display_pipes(pipe_list)
        pipe_list = move_pipe_rect(pipe_list) 
        floor_column -= 1
        display_pipes(pipe_list)
        
        my_screen.blit(my_floor , (0, 570))
        my_screen.blit(my_floor , (floor_column, 570))
        my_screen.blit(my_bird , bird_image_rect)
        update_score()  
        the_score('ACTIVE')       
    else :
        the_score('GAME OVER')
        
    bird_movment += gravity
    bird_image_rect.centery += bird_movment
    if floor_column <= -288:
        floor_column = 0
    pygame.display.update()
    time_game.tick(79)






