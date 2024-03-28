import graphelib
import matplotlib.pyplot as plt
import random

#Create graphe
graphe = graphelib.Graphe()
graphe.lire_villes()
graphe.lire_routes()

#Create carte
carte = graphelib.Carte(graphe)
carte.afficher()
nbNodes = len(graphe.dic_noeud)
dep = random.randrange(1, nbNodes)
arr = random.randrange(1, nbNodes)
noeud_depart = graphe.dic_noeud[dep]
noeud_arrive = graphe.dic_noeud[arr]

dist_dijkstra, prec_dijkstra, cpt_dijkstra = graphelib.dijkstra(graphe, noeud_depart, noeud_arrive)
liste_noeud_dijkstra = graphelib.chemin(dist_dijkstra, prec_dijkstra , noeud_depart, noeud_arrive)

carte.afficher_chemin(liste_noeud_dijkstra, color="red")
plt.show()

dist_astar, prec_astar, cpt_astar = graphelib.Astar(graphe, noeud_depart, noeud_arrive)
liste_noeud_astar = graphelib.chemin(dist_astar, prec_astar, noeud_depart, noeud_arrive)
carte.afficher_chemin(liste_noeud_astar, color="red")



print("Pour aller de {} a {} ".format(noeud_depart.chef_lieu, noeud_arrive.chef_lieu))
print("dijkstra a parcouru: {} noeuds".format(cpt_dijkstra))
print("Astar a parcouru: {} noeuds".format(cpt_astar))
plt.show()