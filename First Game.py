# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 13:57:10 2021

@author: Fahad
"""

import pygame
import random
from pygame import mixer
import sys
import time

pygame.init()

screen = pygame.display.set_mode((1536,865))

background = pygame.image.load('D:/GAME/Images/PSLPIC.jpg')
background = pygame.transform.scale(background,(1536,865))

icon = pygame.image.load('D:/GAME/Icons/BALL.png')
pygame.display.set_icon(icon)
pygame.display.set_caption("PSL")

FONT = pygame.font.Font('D:/GAME/FONTS/FONT 1.ttf',80)
b = FONT.render('FAHAD GAMING',True,(0,255,255))

# screen.fill((0,0,102))
# screen.blit(b,(95,350))
# pygame.display.update()
# time.sleep(3)

# PSLL = mixer.Sound('D:/GAME/Sounds/PSL.mpeg')
# PSLL.play()
# screen.blit(background,(0,0))
# pygame.display.update()
# time.sleep(4)

# mixer.music.load('D:/GAME/Songs/Startup.mpeg')
# mixer.music.play()

enemy1 = pygame.image.load('D:/GAME/Images/LAHORE.jpg')
enemy1 = pygame.transform.scale(enemy1,(80,60))

enemy2 = pygame.image.load('D:/GAME/Images/ISLAMABAD.jpg')
enemy2 = pygame.transform.scale(enemy2,(80,60))

enemy3 = pygame.image.load('D:/GAME/Images/PESHAWAR.jpg')
enemy3 = pygame.transform.scale(enemy3,(85,60))

enemy4 = pygame.image.load('D:/GAME/Images/MULTAN.jpg')
enemy4 = pygame.transform.scale(enemy4,(80,60))

enemy5 = pygame.image.load('D:/GAME/Images/QUETTA.jpg')
enemy5 = pygame.transform.scale(enemy5,(80,60))

enemy6= pygame.image.load('D:/GAME/Images/KARACHI.jpg')
enemy6 = pygame.transform.scale(enemy6,(80,60))

# *********************************************************************************************************** #

def Back(r):
    x = (0,255,0)
    y = (255,255,0)
    if r == 0:
        a = y
        b = y
        c = y
        d = y
    if r == 1:
        a = x
        b = y
        c = y
        d = y
    if r == 2:
        a = y
        b = x
        c = y
        d = y
    if r == 3:
        a = y
        b = y
        c = x
        d = y
    if r == 4:
        a = y
        b = y
        c = y
        d = x
    ft = pygame.font.Font('freesansbold.ttf',100)
    resu = ft.render('Resume',True,a)
    rest = ft.render('Restart',True,b)
    sett = ft.render('Settings',True,c)
    mame = ft.render('Main Menu',True,d)
    screen.blit(resu,(520,120))
    screen.blit(rest,(530,270))
    screen.blit(sett,(505,420))
    screen.blit(mame,(450,570))
    pygame.display.update()

def Ree():
    Back(1)
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RETURN:
                    return
                if e.key == pygame.K_UP:
                    Mam()
                if e.key == pygame.K_DOWN:
                    Ret()

def Ret():
    Back(2)
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RETURN:
                    Stt()
                if e.key == pygame.K_UP:
                    Ree()
                if e.key == pygame.K_DOWN:
                    Set()

def Set():
    Back(3)
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RETURN:
                    print("Settings")
                if e.key == pygame.K_UP:
                    Ret()
                if e.key == pygame.K_DOWN:
                    Mam()

def Mam():
    Back(4)
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RETURN:
                    m()
                if e.key == pygame.K_UP:
                    Set()
                if e.key == pygame.K_DOWN:
                    Ree()

# *********************************************************************************************************** #

def Win(t):
    ft = pygame.font.Font('D:/GAME/FONTS/FONT 1.ttf',80)
    if t == 0:
        LA = ft.render('Lahore Qalandars',True,(120,255,5))
        screen.blit(LA,(270,150))
        WO = ft.render('Won',True,(120,255,6))
        screen.blit(WO,(610,300))
        YeS()
    if t == 1:
        QU = ft.render('Quetta Galadiators',True,(95,1,130))
        screen.blit(QU,(250,150))
        WO = ft.render('Won',True,(95,1,130))
        screen.blit(WO,(610,300))
        YeS()
    if t == 2:
        KA = ft.render('Karachi Kings',True,(7,82,194))
        screen.blit(KA,(330,150))
        WO = ft.render('Won',True,(7,82,194))
        screen.blit(WO,(610,300))
        YeS()
    if t == 3:
        IS = ft.render('Islamabad Uniteds',True,(255,0,0))
        screen.blit(IS,(250,150))
        WO = ft.render('Won',True,(255,0,0))
        screen.blit(WO,(610,300))
        YeS()
    if t == 4:
        PE = ft.render('Peshawar Zalmi',True,(255,255,0))
        screen.blit(PE,(290,150))
        WO = ft.render('Won',True,(255,255,0))
        screen.blit(WO,(610,300))
        YeS()
    if t == 5:
        MU = ft.render('Multan Sultans',True,(88,159,40))
        screen.blit(MU,(290,150))
        WO = ft.render('Won',True,(88,159,40))
        screen.blit(WO,(610,300))
        YeS()
    pygame.display.update()

def si(t):
    x = (0,255,0)
    y = (255,255,0)
    if t == 0:
        a = y
        b = y
    if t == 1:
        a = x
        b = y
    if t == 2:
        a = y
        b = x
    FONT = pygame.font.Font('freesansbold.ttf',60)
    P = FONT.render("Do you want to play again ?",True,y)
    Y = FONT.render('Yes',True,a)
    N = FONT.render('No',True,b)
    screen.blit(P,(350,500))
    screen.blit(Y,(600,650))
    screen.blit(N,(780,650))
    pygame.display.update()

def YeS():
    si(1)
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RETURN:
                    Stt()
                if e.key == pygame.K_LEFT or e.key == pygame.K_RIGHT:
                    NO()

def NO():
    si(2)
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RETURN:
                    m()
                if e.key == pygame.K_LEFT or e.key == pygame.K_RIGHT:
                    YeS()

# *********************************************************************************************************** #

def Dis(you,enemy2,enemy3,enemy4,enemy5,enemy6,enemy7,team):
    # if team == 1:
    #     screen.fill((255,255,0))
    #     mixer.music.load('D:/GAME/Songs/QALANDARS.mpeg')
    #     mixer.music.play()
    # if team == 2:
    #     screen.fill((255,255,0))
    #     mixer.music.load('D:/GAME/Songs/GALADIATORS.mpeg')
    #     mixer.music.play()
    # if team == 3:
    #     screen.fill((255,255,0))
    #     mixer.music.load('D:/GAME/Songs/KARACHI.mpeg')
    #     mixer.music.play()
    # if team == 4:
    #     screen.fill((255,255,0))
    #     mixer.music.load('D:/GAME/Songs/ISLAMABAD.mpeg')
    #     mixer.music.play()
    # if team == 5:
    #     screen.fill((255,255,0))
    #     mixer.music.load('D:/GAME/Songs/PESHAWAR.mpeg')
    #     mixer.music.play()
    # if team == 6:
    #     screen.fill((255,255,0))
    #     mixer.music.load('D:/GAME/Songs/MULTAN.mpeg')
    #     mixer.music.play()
    Score = 0
    font = pygame.font.Font('freesansbold.ttf',32)
    you = pygame.transform.scale(you,(100,80))

    def show_score(X,Y):
        score = font.render("Score: " + str(Score),True,(255,255,0))
        screen.blit(score,(X,Y))

    def You(X,Y):
        screen.blit(you,(X,Y))

    def Bullet(X,Y):
        screen.blit(bullet,(X,Y))

    def Enemy(PIC,X,Y):
        screen.blit(PIC,(X,Y))

    def Distance(x1,y1,x2,y2):
        distance = (((x1-x2)**2)+((y1-y2)**2))**(1/2)
        if distance < 60:
            return True
        else:
            return False

    #              PLAYER
    you_X = 750
    you_Y = 760
    you_changeX = 0
    you_changeY = 0
    
    #              ENEMY 2
    enemy2_X = random.randint(250,500)
    enemy2_Y = 20
    enemy2_changeX = 0.5
    
    #              ENEMY 3
    enemy3_X = random.randint(500,750)
    enemy3_Y = 20
    enemy3_changeX = 0.5
    
    #              ENEMY 4
    enemy4_X = random.randint(750,1000)
    enemy4_Y = 20
    enemy4_changeX = 0.5
    
    #              ENEMY 5
    enemy5_X = random.randint(1000,1250)
    enemy5_Y = 20
    enemy5_changeX = 0.5
    
    #              ENEMY 6
    enemy6_X = random.randint(0,250)
    enemy6_Y = 20
    enemy6_changeX = 0.5

    #              BULLET
    bullet = pygame.image.load('D:/GAME/Icons/BALL.png')
    bullet = pygame.transform.scale(bullet,(40,40))
    x1 = you_X
    y1 = 760
    bullet_changeY = 0
    bullet_x = you_X
    
    Score = 0
    font = pygame.font.Font('freesansbold.ttf',32)
    x = 1
    running = True
    going = True
    while running:
        if Score == 20:
            x = 2
        if Score == 40:
            x = 3
        if Score == 60:
            x = 4
        if Score == 80:
            x = 5
        screen.fill((0,0,0))
        screen.blit(background, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    screen.fill((0,255,255))
                    Pause = True
                    Back(0)
                    while Pause:
                        for e in pygame.event.get():
                            if e.type == pygame.QUIT:
                                sys.exit()
                            if e.type == pygame.KEYDOWN:
                                if e.key == pygame.K_DOWN:
                                    Ree()
                                    Pause = False
                                    break
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if y1<=0:
                        y1 = 760
                        bullet_x = you_X
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    you_changeX = -5
                if event.key == pygame.K_RIGHT:
                    you_changeX = 5
                if event.key == pygame.K_SPACE:
                    bullet_changeY = 7
                    if y1<=0:
                        y1 = 760
                        bullet_x = you_X
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    you_changeX = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    you_changeY = 0

        you_X += you_changeX
        you_Y += you_changeY
    
        y1 -= bullet_changeY
        
        if you_X <= 10:
            you_X = 10
        if you_X >= 1426:
            you_X = 1426
            
        if enemy6_X <= 10:
            enemy6_changeX = x
        elif enemy6_X >= 1436:
            enemy6_changeX = -x
                    
        if enemy6_X >= 1436:
            enemy6_Y += 65
        if enemy6_X <= 10:
            enemy6_Y += 65
                                
        if enemy2_X <= 10:
            enemy2_changeX = x
        elif enemy2_X >= 1436:
            enemy2_changeX = -x
                    
        if enemy2_X >= 1436:
            enemy2_Y += 65
        if enemy2_X <= 10:
            enemy2_Y += 65
                    
        if enemy3_X <= 10:
            enemy3_changeX = x
        elif enemy3_X >= 1436:
            enemy3_changeX = -x
                    
        if enemy3_X >= 1436:
            enemy3_Y += 65
        if enemy3_X <= 10:
            enemy3_Y += 65
                        
        if enemy4_X <= 10:
            enemy4_changeX = x
        elif enemy4_X >= 1436:
            enemy4_changeX = -x
                    
        if enemy4_X >= 1436:
            enemy4_Y += 65
        if enemy4_X <= 10:
            enemy4_Y += 65
                    
        if enemy5_X <= 10:
            enemy5_changeX = x
        elif enemy5_X >= 1436:
            enemy5_changeX = -x
                    
        if enemy5_X >= 1436:
            enemy5_Y += 65
        if enemy5_X <= 10:
            enemy5_Y += 65
                    
        Condition1 = Distance(bullet_x+15,y1,enemy6_X,enemy6_Y)
        Condition2 = Distance(bullet_x+15,y1,enemy2_X,enemy2_Y)
        Condition3 = Distance(bullet_x+15,y1,enemy3_X,enemy3_Y)
        Condition4 = Distance(bullet_x+15,y1,enemy4_X,enemy4_Y)
        Condition5 = Distance(bullet_x+15,y1,enemy5_X,enemy5_Y)
        ConditionX1 = Distance(you_X,you_Y,enemy6_X,enemy6_Y)
        ConditionX2 = Distance(you_X,you_Y,enemy2_X,enemy2_Y)
        ConditionX3 = Distance(you_X,you_Y,enemy3_X,enemy3_Y)
        ConditionX4 = Distance(you_X,you_Y,enemy4_X,enemy4_Y)
        ConditionX5 = Distance(you_X,you_Y,enemy5_X,enemy5_Y)
        
        if Condition1:
            y1 = -30
            bullet_x = you_X
            Score += 1
            enemy6_X = random.randint(0,250)
            enemy6_Y = 20
                    
        if Condition2:
            y1 = -30
            bullet_x = you_X
            Score += 1
            enemy2_X = random.randint(250,500)
            enemy2_Y = 20
                    
        if Condition3:
            y1 = -30
            bullet_x = you_X
            Score += 1
            enemy3_X = random.randint(500,750)
            enemy3_Y = 20
            
        if Condition4:
            y1 = -30
            bullet_x = you_X
            Score += 1
            enemy4_X = random.randint(750,1000)
            enemy4_Y = 20
                    
        if Condition5:
            y1 = -30
            bullet_x = you_X
            Score += 1
            enemy5_X = random.randint(1000,1250)
            enemy5_Y = 20
            
        if ConditionX1 or ConditionX2 or ConditionX3 or ConditionX4 or ConditionX5:
            while going:
                pygame.display.update()
                going = True
                mixer.music.stop()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_y:
                            Dis(you,enemy2,enemy3,enemy4,enemy5,enemy6,enemy6,team)
                        if event.key == pygame.K_n:
                            Stt()

        Goal = font.render("Goal: " + str(100),True,(255,255,0))
        screen.blit(Goal,(1370,10))
        show_score(10,10)
        enemy6_X += enemy6_changeX
        enemy2_X += enemy2_changeX
        enemy3_X += enemy3_changeX
        enemy4_X += enemy4_changeX
        enemy5_X += enemy5_changeX
        Bullet(bullet_x+10,y1)
        You(you_X,you_Y)
        Enemy(enemy6,enemy6_X,enemy6_Y)
        Enemy(enemy2,enemy2_X,enemy2_Y)
        Enemy(enemy3,enemy3_X,enemy3_Y)
        Enemy(enemy4,enemy4_X,enemy4_Y)
        Enemy(enemy5,enemy5_X,enemy5_Y)
        pygame.display.update()

        if Score >= 100:
            while True:
                screen.fill((255,255,255))
                if team == 1:
                    Win(0)
                if team == 2:
                    Win(1)
                if team == 3:
                    Win(2)
                if team == 4:
                    Win(3)
                if team == 5:
                    Win(4)
                if team == 6:
                    Win(5)

# *********************************************************************************************************** #

def Team(team):
    x = (0,255,0)
    y = (255,255,0)
    if team == 'a':
        a = y
        b = y
        c = y
        d = y
        e = y
        f = y
    if team == 'l':
        a = x
        b = y
        c = y
        d = y
        e = y
        f = y
    if team == 'q':
        a = y
        b = x
        c = y
        d = y
        e = y
        f = y
    if team == 'k':
        a = y
        b = y
        c = x
        d = y
        e = y
        f = y
    if team == 'i':
        a = y
        b = y
        c = y
        d = x
        e = y
        f = y
    if team == 'p':
        a = y
        b = y
        c = y
        d = y
        e = x
        f = y
    if team == 'm':
        a = y
        b = y
        c = y
        d = y
        e = y
        f = x
    FONT = pygame.font.Font('freesansbold.ttf',80)
    FonT = pygame.font.Font('freesansbold.ttf',90)
    C = FonT.render('Choose Your Team', True, (255,255,255))
    screen.blit(C,(100,20))
    L = FONT.render('Lahore',True,a)
    screen.blit(L,(350,150))
    Q = FONT.render('Quetta',True,b)
    screen.blit(Q,(350,250))
    K = FONT.render('Karachi',True,c)
    screen.blit(K,(330,350))
    I = FONT.render('Islamabad',True,d)
    screen.blit(I,(270,450))
    P = FONT.render('Peshawar',True,e)
    screen.blit(P,(300,550))
    M = FONT.render('Multan',True,f)
    screen.blit(M,(360,650))
    pygame.display.update()

def La():
    Team('l')
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_BACKSPACE:
                    m()
                if e.key == pygame.K_RETURN:
                    Dis(enemy1,enemy2,enemy3,enemy4,enemy5,enemy6,enemy6,1)
                if e.key == pygame.K_UP:
                    Mu()
                if e.key == pygame.K_DOWN:
                    Qu()

def Qu():
    Team('q')
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_BACKSPACE:
                    m()
                if e.key == pygame.K_RETURN:
                    Dis(enemy5,enemy1,enemy3,enemy4,enemy2,enemy6,enemy6,2)
                if e.key == pygame.K_UP:
                    La()
                if e.key == pygame.K_DOWN:
                    Ka()

def Ka():
    Team('k')
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_BACKSPACE:
                    m()
                if e.key == pygame.K_RETURN:
                    Dis(enemy6,enemy1,enemy3,enemy4,enemy5,enemy2,enemy2,3)
                if e.key == pygame.K_UP:
                    Qu()
                if e.key == pygame.K_DOWN:
                    Is()

def Is():
    Team('i')
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_BACKSPACE:
                    m()
                if e.key == pygame.K_RETURN:
                    Dis(enemy2,enemy1,enemy3,enemy4,enemy5,enemy6,enemy6,4)
                if e.key == pygame.K_UP:
                    Ka()
                if e.key == pygame.K_DOWN:
                    Pe()

def Pe():
    Team('p')
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_BACKSPACE:
                    m()
                if e.key == pygame.K_RETURN:
                    Dis(enemy3,enemy6,enemy1,enemy4,enemy5,enemy2,enemy2,5)
                if e.key == pygame.K_UP:
                    Is()
                if e.key == pygame.K_DOWN:
                    Mu()

def Mu():
    Team('m')
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_BACKSPACE:
                    m()
                if e.key == pygame.K_RETURN:
                    Dis(enemy4,enemy1,enemy3,enemy6,enemy5,enemy2,enemy2,6)
                if e.key == pygame.K_UP:
                    Pe()
                if e.key == pygame.K_DOWN:
                    La()

def Stt():
    screen.fill((0,0,0))
    Team('a')
    while True:
        screen.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    m()
                if event.key == pygame.K_DOWN:
                    La()

# *********************************************************************************************************** #

def insi(t):
    x = (0,255,0)
    y = (255,255,0)
    if t == 0:
        a = y
        b = y
    if t == 1:
        a = x
        b = y
    if t == 2:
        a = y
        b = x
    FONT = pygame.font.Font('freesansbold.ttf',60)
    Y = FONT.render('Yes',True,a)
    N = FONT.render('No',True,b)
    screen.blit(Y,(580,500))
    screen.blit(N,(880,500))
    pygame.display.update()

def Ye():
    insi(1)
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RETURN:
                    sys.exit()
                if e.key == pygame.K_LEFT or e.key == pygame.K_RIGHT:
                    No()

def No():
    insi(2)
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RETURN:
                    m()
                if e.key == pygame.K_LEFT or e.key == pygame.K_RIGHT:
                    Ye()

def SURE():
    screen.fill((0,0,0))
    FONT = pygame.font.Font('freesansbold.ttf',70)
    S = FONT.render('Are you sure ?',True,(255,255,0))
    screen.blit(S,(530,250))
    insi(0)
    pygame.display.update()
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_LEFT:
                    Ye()
                if e.key == pygame.K_RIGHT:
                    No()

# *********************************************************************************************************** #

def DISPL(sta):
    x = (0,255,0)
    y = (255,255,0)
    if sta == 1:
        a = y
        b = y
        c = y
        d = y
    if sta == 2:
        a = x
        b = y
        c = y
        d = y
    if sta == 3:
        a = y
        b = x
        c = y
        d = y
    if sta == 4:
        a = y
        b = y
        c = x
        d = y
    if sta == 5:
        a = y
        b = y
        c = y
        d = x
    FONT = pygame.font.Font('freesansbold.ttf',100)
    Start = FONT.render('Start',True,a)
    screen.blit(Start,(630,55))
    Control = FONT.render('Controls',True,b)
    screen.blit(Control,(540,240))
    Instruction = FONT.render('Instructions',True,c)
    screen.blit(Instruction,(445,430))
    Exit = FONT.render('Quit',True,d)
    screen.blit(Exit,(650,630))
    pygame.display.update()

def St():
    DISPL(2)
    while True:
        X, Y = pygame.mouse.get_pos()
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
            if 545<X<970 and 245<Y<325:
                Co()
            if 450<X<1050 and 425<Y<515:
                In()
            if 655<X<865 and 630<Y<715:
                Ex()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RETURN:
                    Stt()
                if e.key == pygame.K_UP:
                    Ex()
                if e.key == pygame.K_DOWN:
                    Co()

def Co():
    DISPL(3)
    while True:
        X, Y = pygame.mouse.get_pos()
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
            if 630<X<865 and 55<Y<140:
                St()
            if 450<X<1050 and 425<Y<515:
                In()
            if 655<X<865 and 630<Y<715:
                Ex()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RETURN:
                    print("Con")
                if e.key == pygame.K_UP:
                    St()
                if e.key == pygame.K_DOWN:
                    In()

def In():
    DISPL(4)
    while True:
        X, Y = pygame.mouse.get_pos()
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
            if 630<X<865 and 55<Y<140:
                St()
            if 545<X<970 and 245<Y<325:
                Co()
            if 655<X<865 and 630<Y<715:
                Ex()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RETURN:
                    print("Instr")
                if e.key == pygame.K_UP:
                    Co()
                if e.key == pygame.K_DOWN:
                    Ex()

def Ex():
    DISPL(5)
    while True:
        X, Y = pygame.mouse.get_pos()
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
            if 630<X<865 and 55<Y<140:
                St()
            if 545<X<970 and 245<Y<325:
                Co()
            if 450<X<1050 and 425<Y<515:
                In()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RETURN:
                    SURE()
                if e.key == pygame.K_UP:
                    In()
                if e.key == pygame.K_DOWN:
                    St()

def m():
    screen.fill((0,0,0))
    DISPL(1)
    while True:
        for e in pygame.event.get():
            screen.fill((0,0,0))
            X, Y = pygame.mouse.get_pos()
            if e.type == pygame.QUIT:
                sys.exit()
            # if e.type == pygame.MOUSEBUTTONDOWN:
            #     if e.button == 1 and 380<X<630 and 55<Y<145:
            #         Stt()
            #     if e.button == 1 and 285<X<725 and 240<Y<330:
            #         while True:
            #             screen.blit(background,(0,0))
            #             pygame.display.update()
            #             for event in pygame.event.get():
            #                 if event.type == pygame.KEYDOWN:
            #                     if event.key == pygame.K_BACKSPACE:
            #                         m()
            #     if e.button == 1 and 410<X<600 and 625<Y<720:
            #         while True:
            #             Sure = pygame.image.load('D:/GAME/Images/Sure.jpeg')
            #             Sure = pygame.transform.scale(Sure,(800,800))
            #             screen.blit(Sure,(100,0))
            #             pygame.display.update()
            #             for event in pygame.event.get():
            #                 if event.type == pygame.MOUSEBUTTONDOWN:
            #                     if event.button == 1:
            #                         sys.exit()
            #                     if event.button == 1:
            #                         m()
            if 630<X<865 and 55<Y<140:
                St()
            if 545<X<970 and 245<Y<325:
                Co()
            if 450<X<1050 and 425<Y<515:
                In()
            if 655<X<865 and 630<Y<715:
                Ex()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_DOWN:
                    St()
                if e.key == pygame.K_UP:
                    Ex()
m()
