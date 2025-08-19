TAFF3:
    Ecrire un programme qui permet d'évaluer une note saisie au clavier:
    si la note est supérieure ou égal à 10 alors il affiche validé, sinon il affiche non validé
    NB: la note est comprise entre 0 et 20.

note=float(input("entrer la note"))
if note<=20 and note>=10:
    print("valide")
    elif note <10 and note>=0:
        print("non valide")
        else:
            print("la note est incorrect")
