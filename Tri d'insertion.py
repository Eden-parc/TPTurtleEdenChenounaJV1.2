#La fonction de tri-->

def InsertionTri(liste):
    res=[liste[0]]
    

    for i in liste[1:] :
        for k in range(len(res)) :
            
            if i<res[j]:            #Comparaison entre le dernier index et le premier index de la liste
                res.insert(j,i)
                break
            elif k==(len(res)-1):   #C'est pour le moment ou l'on arrive à la fin de la liste
                res.append(i)
    return res