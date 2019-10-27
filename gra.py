#  -*- coding: utf-8 -*-
import sys, pygame, random
from pygame.locals import *

pygame.init()
pygame.display.set_mode((800, 600)) #rozmiar okna
pygame.display.set_caption("moja gra") #tytul

okienko = pygame.display.get_surface() # powierzchnia okna

prostokacik = pygame.Surface((80, 20)) #rysowanie prostokata
paletka=pygame.image.load("./paletka.png")
prostokacik.fill((255, 255, 255)) #wypelnianie kolorem
prostokacik.blit(pygame.transform.scale(paletka,(80,20)),(0,0)) #transformuje obrazek mondre
pXY = prostokacik.get_rect() #nadawanie koordynatow
pXY.x = 100 #poczatkowy x prostokata
pXY.y = 150 #poczatkowy y prostokata

pilka = pygame.image.load("./logo.png") #logo zsti
bXY = pilka.get_rect() #dodanie ksztaltu do loga
bXY.x = 100 #koordynaty x loga
bXY.y = 400 #koordynaty y loga

bx,by = 2,2 #wektor po jakim sie logo porusza
px=5 #wektor paletki
pkt=0 #punkty
czcionka=pygame.font.SysFont("comicsansms", 44) #dodanie czcionki
tlo = pygame.image.load("./tlo.jpeg") #ladowanie tla
def punktuj(): #funkcja do punktow
    tekst = czcionka.render(str(pkt),True,(255,255,255)) #rysowanie czcionki
    tXY = tekst.get_rect() #nadanie ksztaltu
    tXY.center=(100,40) #umiejscownienie
    okienko.blit(tekst, tXY) #wyswietlenie

pygame.display.flip() #wyswietlanie

fps = pygame.time.Clock()   #licznik fps
while 1:
    for zdarzenie in pygame.event.get():    #operacje na zdarzeniach
        if zdarzenie.type == QUIT:
            sys.exit(0) #wyjscie z kodem 0
        if zdarzenie.type == KEYDOWN:
            if zdarzenie.key == K_RIGHT:
                px=5
            if zdarzenie.key == K_LEFT:
                px=-5
            if zdarzenie.key == K_DOWN:
                px=0

       # if zdarzenie.type == KEYUP:
        #    pXY.y-=100
    if pXY.colliderect(bXY): #sprawdzanie kolizji
        by=3


    okienko.fill((128, 128, 128)) # odswiezenie tla
    okienko.blit(tlo, (0,0))
    pXY.x +=px
    okienko.blit(prostokacik, pXY)
    bXY.x+=bx
    bXY.y+=by
    if bXY.x>750 or bXY.x<5:
        bx*=-1
    bXY.y+=by
    if bXY.y>520 :
        by*=-1
        bx = random.randint(2,7)
        pkt+=1
    if bXY.y<-100:
        pkt-=5
        by*=-1
        bx = random.randint(2, 7)

    okienko.blit(pilka, bXY) #rysowanie loga
    punktuj() #punkty
    pygame.display.update() #aktualizacja powierzchni
    fps.tick(60) #ile fps
