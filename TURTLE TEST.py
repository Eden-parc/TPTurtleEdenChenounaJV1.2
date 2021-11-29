import turtle
import random
turtle.delay(0)
Tortue= turtle.Turtle()

def carre (tortue):
    for i in range(4):
        tortue.forward(100)

def rond (tortue):
    for i in range(360):
        tortue.forward(1)

def escargotCarre (tortue,tour):
    for i in range(tour*4):
        tortue.forward(10+i*5)
        tortue.left(90)

def escargotRond(tortue,tour):
    for i in range (tour*360):
        tortue.forward(1+i/1000)
        tortue.left(1)


def marcheAléa(tortue):
    tortue.forward(10)
    angle=random.randint(0,4) 
    tortue.left(angle*90)

def listeTortue (n):
    liste=[]
    for i in range(n):
        liste.append(turtle.Turtle())
    return liste

def Couleur (liste):
    for i in liste:
        i.color(random.random(),random.random(),random.random())


Maliste= listeTortue(15)
Couleur(Maliste)

while 1:
    marcheAléa(Tortue)
    for i in Maliste:
        marcheAléa(i)





input()