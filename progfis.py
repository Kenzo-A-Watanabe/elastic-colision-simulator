#from re import X
#from tkinter import Y
from math import sqrt
import pygame
from random import randint
import numpy as np
from math import pow

def atualizapos():
    for i in range(nbolas):
        bola[i].posicao=bola[i].posicao + bola[i].v
def criabola():
    for i in range(nbolas):
        pygame.draw.circle(window,(0,bola[i].m,bola[i].m*10),(bola[i].posicao),bola[i].raio)
def confereparede():
        for i in range(nbolas):
            if bola[i].posicao[0] + bola[i].raio >= 600:
                bola[i].v[0] = bola[i].v[0] * (-1)
                bola[i].posicao[0] -= (bola[i].posicao[0] + bola[i].raio - 600) 
            elif bola[i].posicao[0] - bola[i].raio <= 0:
                bola[i].v[0] = bola[i].v[0] * (-1)
                bola[i].posicao[0] -= (bola[i].posicao[0] - bola[i].raio) 
                #bola[i].posicao = bola[i].posicao + bola[i].v       
            elif bola[i].posicao[1] + bola[i].raio >= 600:
                bola[i].v[1] = bola[i].v[1] * (-1)
                bola[i].posicao[1] -= (bola[i].posicao[1] + bola[i].raio - 600)
                #bola[i].posicao = bola[i].posicao + bola[i].v
            elif bola[i].posicao[1] - bola[i].raio <= 0:
                bola[i].v[1] = bola[i].v[1] * (-1)
                bola[i].posicao[1] -= (bola[i].posicao[1] - bola[i].raio)  
                #bola[i].posicao = bola[i].posicao + bola[i].v


def verificacolisao():
    j=0
    while j<(nbolas-1):
        k=j+1
        while k<nbolas:
            a = bola[j].posicao[0] - bola[k].posicao[0]
            b = bola[j].posicao[1] - bola[k].posicao[1]
            c = sqrt(pow(a, 2) + pow(b, 2))
            if(bola[j].raio +bola[k].raio+1>=c+1):
                eixox=np.array([bola[k].posicao[0]-bola[j].posicao[0],bola[k].posicao[1]-bola[j].posicao[1]])
                eixoy=np.array([bola[k].posicao[1]-bola[j].posicao[1],bola[j].posicao[0]-bola[k].posicao[0]])
                normy=np.sqrt(sum(eixoy**2))
                normx=np.sqrt(sum(eixox**2))
                v1y=(np.dot(bola[j].v,eixoy)/normy**2)*eixoy
                v2y=(np.dot(bola[k].v,eixoy)/normy**2)*eixoy
                v1x=(np.dot(bola[j].v,eixox)/normx**2)*eixox
                v2x=(np.dot(bola[k].v,eixox)/normx**2)*eixox
                nv1x=np.add((((bola[j].m-bola[k].m)/(bola[j].m+bola[k].m))*v1x),(2*bola[k].m/(bola[j].m+bola[k].m))*v2x)
                nv2x=np.add(((2*bola[j].m/(bola[j].m+bola[k].m))*v1x),(((bola[k].m-bola[j].m)/(bola[j].m+bola[k].m))*v2x))
                vfinal1=np.add(v1y,nv1x)
                vfinal2=np.add(v2y,nv2x)
                bola[j].v=vfinal1
                bola[j].posicao=bola[j].posicao+bola[j].v
                bola[k].v=vfinal2
                bola[k].posicao=bola[k].posicao+bola[k].v
                
            k+=1
        j+=1



class Bola:
        def __init__(self, x, y, vx, vy, raio,m):
            self.posicao = np.array([x, y])
            self.v=np.array([vx, vy])
            self.raio=raio
            self.m=m



        
bola=[]
nbolas=int(input())

pygame.init()
window=pygame.display.set_mode((600,600))
clock=pygame.time.Clock()
fps=120
deucerto=0
while deucerto==0:
    for i in range(nbolas):
        bola.append(Bola(randint (20,580),randint(20,580),randint(-4,4),randint(-4,4),randint(8,25),randint(1,24)))
    j=0
    deucerto=1
    while j<(nbolas-1):
        k=j+1
        while k<nbolas:
            a = bola[j].posicao[0] - bola[k].posicao[0]
            b = bola[j].posicao[1] - bola[k].posicao[1]
            c = sqrt(pow(a, 2) + pow(b, 2))
            if(bola[j].raio +bola[k].raio>c-1):
                bola[j].posicao = np.array([randint(20,580), randint(20,580)])
                deucerto=0
            k+=1
        j+=1


running=True
while running:
    clock.tick(fps)
    window.fill((0,160,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
    criabola()
    verificacolisao()
    confereparede()  
    pygame.display.update()
    atualizapos()
pygame.quit
