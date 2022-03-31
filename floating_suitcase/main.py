import pygame
from pygame import mixer
from random import randint,shuffle

#coords
x = 800; y = 450

#initiate
pygame.init()
mixer.init()

#load
icon = pygame.image.load("ico_suitcase.ico")
suitcase = pygame.image.load("images/suitcase.png") #100x82
open_suitcase = pygame.image.load("images/open_suitcase.png") #81x83
key = pygame.image.load("images/gold_key.png") #15x25
red_hat = pygame.image.load("images/red_hat.png") #50x40
pink_panties = pygame.image.load("images/pink_panties.png") #60x30
yellow_trousers = pygame.image.load("images/yellow_trousers.png") #40x120
green_tshirt = pygame.image.load("images/green_tshirt.png") #80x80
background = pygame.image.load("background/background.png")
introo = pygame.image.load("images/introo.png")
introo2 = pygame.image.load("images/introo2.png")
font = pygame.font.Font("fonts/Pixel.ttf",30)
font2 = pygame.font.Font("fonts/Pixel.ttf",25)
red = pygame.image.load("images/red.png")
gray = pygame.image.load("images/gray.png")
heart = pygame.image.load("images/heart.png")
start = pygame.image.load("images/start.png")
crash_sound = pygame.mixer.Sound("music/bonk.mp3")
point_sound = pygame.mixer.Sound("music/point.mp3")

def crash():
    pygame.mixer.Sound.play(crash_sound)

def point():
    pygame.mixer.Sound.play(point_sound)

screen = pygame.display.set_mode((x, y))
pygame.display.set_icon(icon)
pygame.display.set_caption("Floating Suitcase")
clock = pygame.time.Clock()

spd = 30 #suitcase speed
key_spd = 10 #key speed
speeds = [5, 10] #background speed
speeds_clth = [] #clothes speed

highscore_ez = []
highscore_norm = []
highscore_hard = []
highscore_imp = []

def autro():
    global i, end, hardiness
    i = 0
    omt = False #one more time... :D

    if end:
        music = "win"
        mixer.music.load("music/"+music+".mp3")
        mixer.music.play(-1)
    
    elif end == False:
        music = "lose"
        mixer.music.load("music/"+music+".mp3")
        mixer.music.play(-1)

    while True:
        #moving the screen
        screen.blit(background,(i,0))
        screen.blit(background,(x+i,0))
        if (i==-x):
            screen.blit(background,(x+i,0))
            i = 0
        i -= 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        if end:
            winner = font.render('Congratulations!!!', True,"green")
            reaction = winner.get_rect()
            reaction.center = (x/2, y/2)
            screen.blit(winner, reaction)

        elif end == False:
            loser = font.render('You lost', True,"red")
            screen.blit(gray,(0,0))
            textRect4 = loser.get_rect()
            textRect4.center = (x/2, y/2)
            screen.blit(loser, textRect4)

        continew = font.render('To end, press DELETE, to start, press ENTER', True,"yellow")
        contirect = continew.get_rect()
        contirect.center = (x/2, (y/2)+30)
        screen.blit(continew, contirect)

        if hardiness == "easy":
            fontt = "green"
            highscored = highscore_ez
        elif hardiness == "normal":
            fontt = "grey"
            highscored = highscore_norm
        elif hardiness == "hard":
            fontt = "purple"
            highscored = highscore_hard
        elif hardiness == "impossible":
            fontt = "red"
            highscored = highscore_imp


        scoring = font.render('highscore: '+str(max(highscored)), True,"yellow")
        scorerect = scoring.get_rect()
        scorerect.center = (x/2, 30)
        screen.blit(scoring, scorerect)

        scoring_actual= font.render('score: '+str(highscored[len(highscored)-1]), True,"yellow")
        scorerect_actual = scoring_actual.get_rect()
        scorerect_actual.center = (x/2, 60)
        screen.blit(scoring_actual, scorerect_actual)

        hardness = font.render(hardiness, True, fontt)
        test_hardness = hardness.get_rect()
        test_hardness.center = (x/2, 100)
        screen.blit(hardness, test_hardness)

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_DELETE]:
            break

        elif pressed[pygame.K_RETURN]:
            omt = True
            break

        pygame.display.flip()
        clock.tick(60)

    if omt:
        intro()
        
    pygame.quit()

def gameloop():
    global hardiness,x,y,done, time, i,spd,key_spd,end

    clothes = [red_hat, pink_panties, yellow_trousers, green_tshirt]
    #shuffle(clothes)

    x_case = (x/2)-50; y_case = (y/2)+60
    x_other1 = -50; y_other1 = randint(40,y-40)
    x_other2 = randint(30,x-30); y_other2 = -60
    x_other3 = randint(40,x-40); y_other3 = y+120
    x_other4 = x+80; y_other4 = randint(80,y-80)
    x_key = -50; y_key = -50

    end = False
    time = 1
    done = False
    state = False
    i = 0
    score = 0
    key_react = False

    clth_one = True
    clth_two = True
    clth_three = True
    clth_four = True

    if hardiness == "impossible":
        hp = 16
        mixer.music.load("music/megalovania.mp3")
        mixer.music.play(-1)
        time1 = 150
        time2 = 300
        key_time = 3050

    elif hardiness == "hard":
        hp = 4
        mixer.music.load("music/blue.mp3")
        mixer.music.play(-1)
        time1 = 310
        time2 = 640
        key_time = 4200

    elif hardiness == "normal":
        hp = 8
        mixer.music.load("music/crazy_train.mp3")
        mixer.music.play(-1)
        time1 = 250
        time2 = 520
        key_time = 3500

    elif hardiness == "easy":
        hp = 16
        mixer.music.load("music/axel_f.mp3")
        mixer.music.play(-1)
        time1 = 120
        time2 = 250
        key_time = 3250

    #find "key times"
    key_times = [k for k in range(int(key_time/5),key_time+1,int(key_time/5))]

    while not done:

        #delay
        pygame.time.delay(50)
        
        if time >= time1:
            score +=1

        #arrows
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and y_case >= 0:
            y_case -= spd
        if keys[pygame.K_DOWN] and (y_case+82) <= y:
            y_case += spd
        if keys[pygame.K_RIGHT] and (x_case+100) <= x:
            x_case += spd
        if keys[pygame.K_LEFT] and x_case >= 0:
            x_case -= spd

        #awsd
        if keys[pygame.K_w] and y_case >= 0:
            y_case -= spd
        if keys[pygame.K_s] and (y_case+82) <= y:
            y_case += spd
        if keys[pygame.K_d] and (x_case+100) <= x:
            x_case += spd
        if keys[pygame.K_a] and x_case >= 0:
            x_case -= spd

        #end
        if keys[pygame.K_DELETE]:
            pygame.quit()

        #rectangles behind the screen
        if clth_one:
            hat_b = pygame.draw.rect(screen, "black", pygame.Rect(x_other1, y_other1, 50, 40), 1)
        if clth_two:
            panties_b = pygame.draw.rect(screen, "black", pygame.Rect(x_other2, y_other2, 60, 30), 1)
        if clth_three:
            trousers_b = pygame.draw.rect(screen, "black", pygame.Rect(x_other3, y_other3, 40, 120), 1)
        if clth_four:
            shirt_b = pygame.draw.rect(screen, "black", pygame.Rect(x_other4, y_other4, 80, 80), 1)

        case_b = pygame.draw.rect(screen, "black", pygame.Rect(x_case, y_case, 100, 82),  1)
        key_b = pygame.Rect(x_key, y_key, 25, 35)
        pick = key_times[0]

        if time >= pick and time <= (key_times[len(key_times)-1])+pick:
            pygame.draw.rect(screen, "black", key_b, 2)
            if y_key >= y:
                x_key = -50; y_key = -50      

        #moving the screen
        screen.blit(background,(i,0))
        screen.blit(background,(x+i,0))
        if (i==-x):
            screen.blit(background,(x+i,0))
            i=0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        #Clothes
        if clth_one:
            screen.blit(clothes[0],(x_other1, y_other1))
            collide = pygame.Rect.colliderect(case_b, hat_b)
        else:
            collide = None

        if clth_two:
            screen.blit(clothes[1],(x_other2, y_other2))
            collide1 = pygame.Rect.colliderect(case_b, panties_b)
        else:
            collide1 = None

        if clth_three:
            screen.blit(clothes[2],(x_other3, y_other3))
            collide2 = pygame.Rect.colliderect(case_b, trousers_b)
        else:
            collide2 = None

        if clth_four:
            screen.blit(clothes[3],(x_other4, y_other4))
            collide3 = pygame.Rect.colliderect(case_b, shirt_b)
        else:
            collide3 = None

        #suitcase 
        if key_react == True:
            screen.blit(open_suitcase,(x_case, y_case))
        if key_react == False:
            screen.blit(suitcase,(x_case, y_case))

        #key
        if time >= pick and time < key_times[len(key_times)-1]:
            screen.blit(key,(x_key, y_key))
            x_key += key_spd
            y_key += key_spd
            if y_key >= y:
                x_key = -50; y_key = -50
                if len(key_times) != 0:
                    key_times.remove(pick)                       

        #key collision
        collide_key = pygame.Rect.colliderect(case_b, key_b)
        if collide_key:
            key_react = True
            x_key = x+50
            y_key = y+50
            if len(key_times) != 0:
                key_times.remove(pick)

        #title
        text = font.render("Floating Suitcase", True,"orange")
        textRect = text.get_rect()
        textRect.center = (x/2, 40)
        screen.blit(text, textRect)

        #score
        scoring = font.render("score: "+str(score), True,"white")
        textRect2 = scoring.get_rect()
        textRect2.center = (x/2, 70)
        screen.blit(scoring, textRect2)

        #timer
        timing2 = font.render("time: "+str(time), True,"black")
        textRecttime = timing2.get_rect()
        textRecttime.center = (x-90, 30)
        screen.blit(timing2, textRecttime)

        #level
        if hardiness == "easy":
            fontt = "green"
        elif hardiness == "normal":
            fontt = "grey"
        elif hardiness == "hard":
            fontt = "purple"
        elif hardiness == "impossible":
            fontt = "red"

        hardness = font.render(hardiness, True, fontt)
        test_hardness = hardness.get_rect()
        test_hardness.center = (x/2, 100)
        screen.blit(hardness, test_hardness)

        #hearts
        for j in range(hp+1):
            screen.blit(heart,(x-(j*50),y-45))

        """if hp == 1:
            screen.blit(red,(0,0))"""

        if time < time1-40:
            screen.blit(introo,((x/2)-400,-40))

        if clth_one == False and clth_two == False and clth_three == False and clth_four == False: #or time == key_time:
            if hardiness == "easy":
                highscore_ez.append(score)
            if hardiness == "normal":
                highscore_norm.append(score)
            if hardiness == "hard":
                highscore_hard.append(score)
            if hardiness == "impossible":
                highscore_imp.append(score)
            end = True
            state = True
            done = True

        #changing speed to music and levels
        if  time >= time1 and time < time2:
            spd_clth = speeds_clth[0]
            i-=speeds[0]
        if  time >= time2:
            spd_clth = speeds_clth[1]
            i-=speeds[1]

        if time >= time1:
            x_other1 += spd_clth
            if x_other1 >= x+50:
                x_other1 = -50
                y_other1 = randint(40,y-40)

            y_other2 += spd_clth
            if y_other2 >= y+30:
                x_other2 = randint(30,x-30)
                y_other2 = -60

            y_other3 -= spd_clth
            if y_other3 <= -120:
                x_other3 = randint(40,x-40)
                y_other3 = y + 120
            
            x_other4 -= spd_clth
            if x_other4 <= -80:
                x_other4 = x + 80
                y_other4 = randint(80,y-80)

        if end == False:
            if collide or collide1 or collide2 or collide3:
                if key_react == False:
                    pass
                    crash()
                    hp -= 1
                    x_other1 = -50; y_other1 = randint(40,y-40)
                    x_other2 = randint(30,x-30); y_other2 = -60
                    x_other3 = randint(40,x-40); y_other3 = y+120
                    x_other4 = x+80; y_other4 = randint(80,y-80)

                    if hp == 0:
                        state = True
                        if hardiness == "easy":
                            highscore_ez.append(score)
                        if hardiness == "normal":
                            highscore_norm.append(score)
                        if hardiness == "hard":
                            highscore_hard.append(score)
                        if hardiness == "impossible":
                            highscore_imp.append(score)
                        done = True

                elif key_react:
                    if collide:
                        x_other1 = -100; y_other1 = -100
                        clth_one = False             
                    if collide1:
                        x_other2 = -100; y_other2 = -100
                        clth_two = False      
                    if collide2:
                        x_other3 = -100; y_other3 = -100
                        clth_three = False                  
                    if collide3:
                        x_other4 = -100; y_other4 = -100
                        clth_four = False

                    point()
                    key_react = False
                    
        pygame.display.flip()
        clock.tick(60)
        time += 1

    if state == True:
        autro()

def levels():
    global hardiness, i
    hardiness = ""
    mixer.music.load("music/radioactive.mp3")
    mixer.music.play(-1)
    while True:
        #moving the screen
        screen.blit(background,(i,0))
        screen.blit(background,(x+i,0))
        if (i==-x):
            screen.blit(background,(x+i,0))
            i = 0
        i -= 1

        level_text = font2.render("1 = Easy, 2 = Normal, 3 = Hard, 4 = Impossible", True,"yellow")
        textRectlevel = level_text.get_rect()
        textRectlevel.center = (x/2, y/2)
        screen.blit(level_text, textRectlevel)  

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_1]:
            hardiness = "easy"
            speeds_clth.clear()
            speeds_clth.extend([5,10])
            break

        if pressed[pygame.K_2]:
            hardiness = "normal" 
            speeds_clth.clear()
            speeds_clth.extend([10,15])
            break

        if pressed[pygame.K_3]:
            hardiness = "hard"
            speeds_clth.clear()
            speeds_clth.extend([15,20])
            break

        if pressed[pygame.K_4]:
            hardiness = "impossible"
            speeds_clth.clear()
            speeds_clth.extend([20,25])
            break

        if pressed[pygame.K_DELETE]:
            pygame.quit()

        pygame.display.flip()
        clock.tick(60)
    gameloop()

def intro():
    global i
    x_case = (x/2)-50; y_case = (y/2)+60
    i = 0
    mixer.music.load("music/Pixel.mp3")
    mixer.music.play(-1)
    pygame.mixer.fadeout(100)

    while True:
        #moving the screen
        screen.blit(background,(i,0))
        screen.blit(background,(x+i,0))
        if (i==-x):
            screen.blit(background,(x+i,0))
            i = 0
        i -= 1

        screen.blit(introo2,((x/2)-300,30))
        screen.blit(start,((x/2)-200,100))
        screen.blit(suitcase,(x_case,y_case))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_SPACE]:
            break

        if pressed[pygame.K_DELETE]:
            pygame.quit()

        pygame.display.flip()
        clock.tick(60)
    levels()

intro()