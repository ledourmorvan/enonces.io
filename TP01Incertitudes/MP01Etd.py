###############################################################################
#                                                                             #
#             TP n°1 : paramètres d'un générateur de Thévenin                 #
#                                                                             #
###############################################################################


#%% Cellule n°1 : importations

import numpy as np
from matplotlib import pyplot as plt
import statistics

 
#%% Cellule n°2: incertitude u(R)

tab_R=np.array([,,,,,,,,])# Valeurs de R à saisir en ohm

def u1(R):
    return               #Saisir la formule de calcul des incertitudes

tab_uR=u1(tab_R)         #Calcul des incertitudes pour toutes les valeurs de R  
print('Incertitude pour R=50 ohm:', tab_uR[3],' ohm.')


#%% Cellule n°3 : première estimation de u(rs)
 
def u2(V):
    return               #Saisir la formule de calcul des incertitudes

def u3(U,E,R):
    uU, uE, uR = u2(U), u2(E), u1(R) #Calcul des incertitudes des différentes grandeurs mesurées
    N=5000                           #Nombre de valeurs de rs estimées   
    tab_rs=np.zeros(N)               #Définition du tableau numpy
                                     #Rédiger ici la suite de la fonction
    return tab_rs, mrs,ers

tab,rs,urs =u3(0.9,1.8,50)          #Appel de la fonction u3 avec les valeurs mesurées
plt.title(r'$r_s=$'+str(rs)[0:6]+' $\Omega\qquad u(r_s)=$'+str(urs)[0:6]+' $\Omega$')
plt.hist(tab,bins=41, density=True) #Affichage des résultats sous la forme d'histogrammes.


#%% Cellule n°4 : représentation graphique de Eeff/Ueff en fonction de 1/R

tab_Ueff=np.array([,,,,,,,,])# Valeurs de Ueff en V à saisir
Eeff=                                       # Valeur de Eeff en V à saisir

tab_uUeff=u2(tab_Ueff)                                        # Calcul des incertitudes sur Ueff
uEeff=u2(Eeff)                                                # Calcul de l'incertitudes sur Eeff

def Abscisses(E,tab_U):                                       # Calcul du tableau de valeurs des abscisses
    return tab_U/(E-tab_U)

tab_absc=Abscisses(Eeff,tab_Ueff)                             # Appel de la fontion précédente

plt.ylabel(r'$R$ en $\Omega$')
plt.axis([0, 2.5, -0.05, 110]);
plt.xlabel(r'$U_{eff}/(E_{eff}-U_{eff})$')
plt.plot(tab_absc, tab_R,'o', linestyle='none',color = 'b', label = 'Points expérimentaux' )
plt.show()                                                    # Affichage du graphe.


#%% Cellule n°5 : régression linéaire et résidus

def regression(tab_X,tab_Y):                                  # Fonction à compléter
    
    return

rs=regression(tab_absc,tab_R)                                 # Appel de la fontion précédente
tab_residus=                                                  # Formule du calcul des résidus 

plt.title(r'$r_s=$'+str(rs)[0:6]+' $\Omega$')
plt.ylabel(r'Résidus en $\Omega$')
plt.xlabel(r'$U_{eff}/(E_{eff}-U_{eff})$')
plt.errorbar(tab_absc, tab_residus, xerr = 0, yerr = tab_uR, fmt='o', linestyle='none',color = 'r')
plt.show()                                                    # Affichage du graphe.


#%% Cellule n°6 : régression linéaire et écarts normalisés

tab_EcartsNormalises=                                          # Formule du calcul des écarts normalisés 

plt.ylabel(r'Ecarts normalisés')
plt.xlabel(r'$U_{eff}/(E_{eff}-U_{eff})$')
x=np.arange(0,2.5,0.01)    
plt.errorbar(tab_absc, tab_EcartsNormalises, fmt='o', linestyle='none',color = 'b')# Tracé des écarts normalisés
x=np.arange(0,2.5,0.01)                                       # coloriage de la région comprise entre -2 et +2 
plt.fill_between(x, 2,-2, color='0.9')                          
plt.show()                               

#%% Cellule n° 7 : régression linéaire et incertitudes

def incertitudeRegression(tab_U,E,tab_R):                     # Fonction à compléter
    tab_uU, uE, tab_uR = u2(tab_U), u2(E), u1(tab_R)          # Calcul des incertitudes des différentes grandeurs mesurées
    N=5000                                                    # Nombre de valeurs de rs estimées  
    tab_rs=np.zeros(N)                                        # Initialisation du tableau des valeurs de rs
                                                              # Rédiger ici la suite de la fonction
    return tab_rs, mrs,ers

tab,rs,urs =incertitudeRegression(tab_Ueff,Eeff,tab_R)
plt.title(r'$r_s=$'+str(rs)[0:6]+' $\Omega\qquad u(r_s)=$'+str(urs)[0:6]+' $\Omega$')
plt.hist(tab,bins=41, density=True)
plt.show()                                                    # Affichage du graphe.
