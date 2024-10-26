import numpy as np

na = int(input("How many of A?"))
nb = int(input("How many of B?"))
tot = int(input("How many total?"))
pa = na/tot
pb = nb/tot
entropy = (-pa * np.log2(pa))+(-pb * np.log2(pb))
print(entropy)
