TAFF4:
ecrire un programme permettant de saisir le prix total HT et de calculer le montant TTC en prenant en compte la réduction et la
TVA = 20%.TTC=tout taxe compris

prix_HT=float(input("entrer le montant HT:"))
prix_TTC=prix_HT + prix_HT*0.2
if prix_TTC>20000:
    prix_TTC=prix_TTC - prix_TTC*0.15
    print("le montant TTC est : ", prix_TTC)
else:
    print("le montant TTC est :", prix_TTC)
entrer le montant HT: 24
le montant TTC est : 28.8


    
