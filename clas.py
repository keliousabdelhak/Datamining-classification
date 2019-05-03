from math import *
from collections import OrderedDict
import matplotlib.pyplot as plt


#Le point qu'on veut ajouter 
x1=(2,3.5)


# k Le nombre de voisins de x1
k=3


#Les deux  cluster c1 et c2 // on peut mettre plus 
c1=[(1.5,2),(3,4),(7,0),(3,6)]
c2=[(1,4),(2,4),(-3,1),(-2,5)]


#Calucle de la distance euclidienne
dic={}
def distance(a,b,c,d):
	dis=sqrt((a-c)**2 + (b-d)**2)
	return dis

# Parcourir c1 et calculer les distances  pour les mettre dans un dictionnaire 
i=1
for c in c1 :
	l= "c1(" + str(i)+")"
	d1=distance(c[0],c[1],x1[0],x1[1])
	dic[l]=d1
	i+=1

# Parcourir c2 et calculer les distances  pour les mettre dans un dictionnaire 
j=1
for c in c2 :
	m= "c2(" + str(j)+")"
	d2=distance(c[0],c[1],x1[0],x1[1])
	dic[m]=d2
	j+=1


# Ordonné les distances dans le dictionnaire (croissant)
ordo = OrderedDict(sorted(dic.items(),key=lambda t: t[1]))


# calcule le nombre de voisin et le clutser qui contient le plus de voisin
ite= 1
voisin_c1=0
voisin_c2=0
for l,v in ordo.items():
	if (ite <= k):
		ite+=1
		if l[1]=="2":
			voisin_c2+=1
		else:
			voisin_c1+=1
	else:
		pass


# Ajouter le point vers le cluster qui lui convient 
deplacer="none"
if voisin_c1<voisin_c2:
	print("x1 va  dans c2")
	deplacer="x1 est dans  c2 "
	c2.append(x1)
else:
	print("x1 va dans c1")
	deplacer="x1 est dans  c1 "
	c1.append(x1)


# affichage du résulatats sur interface 
li_c1_x=[]
li_c1_y=[]
for ele in c1:
	li_c1_x.append(ele[0])
	li_c1_y.append(ele[1])

li_c2_x=[]
li_c2_y=[]
for ele in c2:
	li_c2_x.append(ele[0])
	li_c2_y.append(ele[1])

plt.scatter(li_c1_x, li_c1_y,  c='coral', label='cluster 1')
plt.scatter(li_c2_x, li_c2_y,  c='lightblue', label='cluster 2')
plt.legend()
plt.text(x1[0],x1[1],deplacer)
plt.title('Nuage de points')
plt.xlabel('les x ')
plt.ylabel('les y')
plt.savefig('cluster.png')
plt.show()

#fin de l'algorithme 