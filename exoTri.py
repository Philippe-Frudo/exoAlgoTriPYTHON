#EN COURS DE TRAITEMENT

def tri_a_bulle(tab):
    t = tab
    i = 0
    compteT = len(t)
    while i < compteT:
        j = i + 1
        while j < compteT:
            if t[i] > t[j]:
                # temp = t[j]
                # t[j] = t[i]
                # t[i] = temp
                t[i], t[j] = t[j], t[i]
            j += 1
        i += 1

    nombre_inserer = float(input("Entrer le nombre inseret: "))
    #t.append(nombre_inserer)
    m = nombre_inserer
    y = 0
    while y < compteT+1:
        if m > t[y]:
            temp = t[y]
            t[y] = m
            t[y+1] = temp
            # t[y], t[y] = t[y+1], m
        y += 1
    return t
t1 = tri_a_bulle([2, 7, 3, 4, 1, 21, -20])
for x in t1:
    print(x, end=" ")



#Tri par Selection
def tri(tab, index):
    c = len(tab)
    mini = tab[index]
    #print(mini)
    p = 0
    i = index + 1
    while i < c:
        if mini > tab[i]:
            mini = tab[i]
            p = i
        i += 1
    return p


tab = [2, 3, 4, 7, 1]
k = 0
countTab = len(tab)
while k < countTab:
    tab[k], tab[tri(tab, k)] = tab[tri(tab, k)], tab[k]
    k += 1
for x in tab:
    print(x, end=" ")

#EN ATTENDANT



# A finir
def fusionner(t_left, t_rigth):
    i = j = k = 0
    tab = []
    while (i < len(t_left)) and (j < len(t_rigth)):
        if t_left[i] <= t_rigth[j]:
            tab[k] = t_left[i]
            i += 1
        else:
            tab[k] = t_rigth[j]
            j += 1
        k += 1

    # Ajouter les elements restant de left
    while i < len(t_left):
        tab[k] = t_left[i]
        i += 1
        k += 1

    # Ajouter les elements restant de left
    while j < len(t_rigth):
        tab[k] = t_rigth[j]
        j += 1
        k += 1

    for x in tab:
        print(x)



def triFusion(tab):
    if len(tab) <= 1:
        return tab

    center = len(tab)//2

    #Trier la partie guache
    # tab_Left = triFusion(tab[0:center])
    tab_Left = triFusion(tab[:center])
    print(tab_Left)

    #Trier la partie droite
    # tab_rigth = triFusion(tab[center:len(tab)])
    tab_rigth = triFusion(tab[center:])
    print(tab_rigth)

    return fusionner(tab_Left, tab_rigth)


triFusion([3, 1, 1, 5, 12, 5, 60, 41, 75, 14, 15, 10, 4])