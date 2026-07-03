import matplotlib.pyplot as plt
import numpy as np

# notes = np.array([5, 2, 3])
# print(notes[:2], notes.min()) # Affiche les deux premiers éléments du tableau



# notes = np.random.randint(0,21, 10)
# moyen = np.mean(notes)

# plt.plot(notes)
# plt.axhline(y=moyen, color='r', linestyle='--', label='Moyenne')
# plt.legend()
# plt.show()



# nb = np.random.randint(0, 21, 30)
# print (nb)

# def sup(nombre):
#     nbvalsup = 0
#     valsup = []
#     for valeur in nombre:
#         if valeur > 10:
#             valsup.append(int(valeur)) 
#             nbvalsup += 1
#     return nbvalsup, valsup
# print(sup(nb))

# notes = np.array([8, 12, 15, 9, 18])

# print(notes[notes < 10])



# a = np.random.normal(8, 2, 5000)
# b = np.random.normal(14, 2, 5000)

# plt.hist(a, bins=20, alpha=0.6)
# plt.hist(b, bins=20, alpha=0.6)
# plt.show()

# x = np.arange(0, 10, 0.5)
# bruit = np.random.normal(0, 0.1, len(x))
# y = 2 * x + 1 + bruit
# a, b = np.polyfit(x, y, 1)
# plt.scatter(x, y, label='Données avec bruit')
# plt.plot(x, a * x + b, color='r', label='Modèle linéaire')
# plt.plot(x, 2 * x + 1, color='g')
# plt.show()