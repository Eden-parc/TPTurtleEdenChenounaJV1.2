liste1=[2, 6, 8, 45, 21, 69, 752, 213, 75, 12, 63, 97, 43, 76, 13, 67]

def petit (liste):
    test=liste[0]
    for i in liste:
        if i<test:
            test=i
    return test

def selectiontri (liste):
    liste2=[]
    for i in range(0,len(liste)):
        elem=petit(liste)
        liste.remove(elem)
        liste2.append(elem)
    return liste2

print(selectiontri(liste1))