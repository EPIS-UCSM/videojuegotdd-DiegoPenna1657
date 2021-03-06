import pygame, sys, time, random
from pygame.locals import *

pygame.init()
width = 500
height = 700
play_surface = pygame.display.set_mode((width, height))
background_image = pygame.image.load("back2.png").convert()
bird_image = pygame.image.load("mmmm.png").convert_alpha()
top_pipe = pygame.image.load("pipe_top.png").convert_alpha()
bot_pipe = pygame.image.load("pipe_bot.png").convert_alpha()
fps = pygame.time.Clock()


#Contador
def draw_text(surface, text, size, x, y):
    font = pygame.font.SysFont("serif", size)
    text_surface = font.render(text, True, 'white')
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    surface.blit(text_surface, text_rect)

#Game Over
def show_go_screen():
    play_surface.blit(background_image, [0,0])
    draw_text(play_surface," Flappy Gunter", 65, width //2, height //4)
    draw_text(play_surface, "Press key" , 27, width //2, height // 2)
    
    pygame.display.flip()
    waiting = True
    while waiting:
        fps.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False

#top pipe

def pipe_random_height():
    pipe_h = [random.randint(200,(height/2)-20), random.randint((height/2)+20, height-200)]
    return pipe_h

def main():
    score = 0
    player_pos = [100, 350]
    gravity = 1
    speed = 0
    jump = -30
    game_over = True

    #pipe
    pipe_pos = 700
    pipe_width = 50
    pipe_height = pipe_random_height()

    

    run = True
    while run:
        if game_over == True:
            show_go_screen()
            game_over = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            #CASOS DE PRUEBA
                
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    print (f"El objeto responde a esta tecla")
                if event.key == pygame.K_RIGHT:
                    print (f"El objeto responde a esta tecla")
                if event.key == pygame.K_LEFT:
                    print (f"El objeto responde a esta tecla")
                    
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        speed += jump

        #Down Force
        speed += gravity
        speed *= 0.95
        player_pos[1] += speed

        #pipe
        if pipe_pos >= -20:
            pipe_pos -= 10
        else:
            pipe_pos = 700
            pipe_height = pipe_random_height()
            score += 1

        #Surface
        play_surface.blit(background_image, [0, 0])

        #drawpipe
        play_surface.blit(top_pipe, (pipe_pos, -pipe_height[0]))
        play_surface.blit(bot_pipe, (pipe_pos, pipe_height[1]))

        #player
        play_surface.blit(bird_image, (int(player_pos[0]), int(player_pos[1])))

        
        
        #Collision
        if player_pos[1] <= (-pipe_height[0]+500) or player_pos[1] >= pipe_height[1]:
            if player_pos[0] in list(range(pipe_pos, pipe_pos+pipe_width)):
                print(f"EL JUEGO A TERMINADO. SCORE OBTENID O: {score}")
                score=0
                player_pos = [100, 350]
                pipe_pos = 700
                pipe_width = 50
                game_over=True

        #Marcador
        draw_text(play_surface,"Score :" + str(score), 25, width // 2,10)
        
        #Borders
        if player_pos[1] >= height:
            player_pos[1] = height
            speed = 0
        elif player_pos[1] <= 0:
            player_pos[1] = 0
            speed = 0

        pygame.display.flip()
        fps.tick(25)


main()
pygame.quit()
