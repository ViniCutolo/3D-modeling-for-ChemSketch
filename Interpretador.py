from Leitor import caminho, traducao, organiza
from vpython import sphere, vector, color, cylinder
from random import randint
import math

def desenho(dicio):
    caract={
        "C" : [1, color.gray(0.7)],
        "N" : [1, color.blue],
        "H" : [0.5, color.white],
        "O" : [1, color.red],
        "P" : [1.5, color.orange],
        "S" : [1.5, color.yellow],
        "F" : [0.75, color.purple],
        "Cl" : [1.25, color.green]
    }

    # para fazer-los vibrar, precisamos guarda-los
    lista_de_atomos=[]
    # isso ira armazenar a posição original
    lista_de_pos_or=[]

    fator_de_correc=6
    # vamos definis qual sera a esfera do meio (o vezes dois é so para facilitar de ver)
    x=fator_de_correc*float(dicio["atomo 1"][0])
    y=fator_de_correc*float(dicio["atomo 1"][1])
    z=fator_de_correc*float(dicio["atomo 1"][2])
    posi=[x,y,z]

    # desenhando os atomos
    for i in range(1, dicio["q.atomos"]+1):
        # pegando as informaçoes
        nome = "atomo "+str(i)
        x=fator_de_correc*float(dicio[nome][0])
        y=fator_de_correc*float(dicio[nome][1])
        z=fator_de_correc*float(dicio[nome][2])
        rad=3*caract[dicio[nome][3]][0]
        cor=caract[dicio[nome][3]][1]

        # vamos desenhar a esfera
        lista_de_atomos.append(sphere(
            pos=vector(x-posi[0],y-posi[1],z-posi[2]),
            radius=rad,
            color=cor
            ))

        # vamos guardar a posição original
        lista_de_pos_or.append(vector(x-posi[0],y-posi[1],z-posi[2]))
    
    # desenhando as ligações
    for i in range(1, dicio["q.ligações"]+1):

        # vamos achar os atomos e definir os vetores
        nome = "ligação "+str(i)
        nome_atomo = "atomo "+dicio[nome][0]
        x=fator_de_correc*float(dicio[nome_atomo][0])
        y=fator_de_correc*float(dicio[nome_atomo][1])
        z=fator_de_correc*float(dicio[nome_atomo][2])
        atomo_1=vector(x-posi[0],y-posi[1],z-posi[2])

        nome_atomo = "atomo "+dicio[nome][1]
        x=fator_de_correc*float(dicio[nome_atomo][0])
        y=fator_de_correc*float(dicio[nome_atomo][1])
        z=fator_de_correc*float(dicio[nome_atomo][2])
        atomo_2=vector(x-posi[0],y-posi[1],z-posi[2])

        # vamos desenhar a ligação
        if dicio[nome][2]=="1":
            cylinder(
                pos=atomo_1,
                axis=atomo_2-atomo_1,
                raidius=0.01
            )

        elif dicio[nome][2]=="2":
            perpen=prod_vet(atomo_2-atomo_1)*fator_de_correc/4
            cylinder(
                pos=atomo_1+perpen,
                axis=atomo_2-atomo_1,
                raidius=0.01
            )
            cylinder(
                pos=atomo_1-perpen,
                axis=atomo_2-atomo_1,
                raidius=0.01
            )

        elif dicio[nome][2]=="3":
            perpen=prod_vet(atomo_2-atomo_1)*fator_de_correc/3
            cylinder(
                pos=atomo_1+perpen,
                axis=atomo_2-atomo_1,
                raidius=0.01
            )
            cylinder(
                pos=atomo_1-perpen,
                axis=atomo_2-atomo_1,
                raidius=0.01
            )
            cylinder(
                pos=atomo_1,
                axis=atomo_2-atomo_1,
                raidius=0.01
            )
        
    # seja t o tempo e dt a variaçao dele
    t=0
    dt=0.1

    # seja A a amplitude e omega a frequencia angular
    A=0.1

    while True:
        for i in range(0, dicio["q.atomos"]):
            omega=(lista_de_pos_or[i].x+posi[0])**2

            dx=A*math.cos(omega*t)
            dy=A*math.sin(omega*t)
            dz=A*math.cos(omega*t)*math.sin(omega*t)

            deform=vector(dx,dy,dz)

            lista_de_atomos[i].pos=lista_de_pos_or[i]+deform
        t+=dt
        if t>10:
            t=0
        pass

def prod_vet(vec):
    # vetor aleatorio
    x=randint(-5,5)
    y=randint(-5,5)
    z=randint(-5,5)

    #vetor perpendicular
    xf=y*vec.z-z*vec.y
    yf=z*vec.x-x*vec.z
    zf=x*vec.y-y*vec.x
    return vector(xf,yf,zf)/(math.sqrt(xf**2 + yf**2 + zf**2))
    


def main():
    #vamos colher as informações que precisamos
    lista = traducao(caminho())
    info=organiza(lista)
    desenho(info)
    
    



if __name__=='__main__':
    main()