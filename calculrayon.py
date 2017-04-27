#!/usr/bin/python2.7
from math import


def rayon1(xA, x0, yA, y0, zA, z0):
	return sqrt((xA-x0)^2+(yA-yo)^2+(zA-z0)^2)
	
def lst_memoire=[{'x', 'y', 'z', 'rayon'}]

for i in dicoPDB.keys():
	for j in dicoPDB[i].keys():
		for k in dicoPDB[i][j].keys():
			for l in dicoPDB[i][j][k].keys():
				if l=="CA" :
					xA=dicPDB[i][j][k][l]["x"]
					yA=dicPDB[i][j][k][l]["y"]
					zA=dicPDB[i][j][k][l]["z"]
					
					rayon=rayon1(xA, x0, yA, y0, zA, z0)
					
					lst_memoire.append({'x': x, 'y': y, 'z': z, 'rayon':rayon(x,y,z)})
					

print(max(lst_memoire, key=lambda d: d['rayon']))

					
	

	
