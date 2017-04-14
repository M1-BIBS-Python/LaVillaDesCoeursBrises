#!/usr/bin/env python
#-*- coding : utf8 -*-

# Narjes NALOUTI

from math import sqrt
import string
import re
import matplotlib.pyplot as plt
import numpy as np
import sys
import os

def ParserPDB(PDBFile):

	""" parserPDB : programme permettant de recuperer dans un fichier PDB l'ensemble des atomes de la proteine et leurs coordonnees x, y, z
		Specification qui permet de charger un fichier PDB au format ATOM, parse son contenu pour le sauvegarder dans une variable Python
		Entree : "PDBFile = emplacement du fichier PDB a charger & a parser
		Sortie : un dictionnaire contenant les informations structurelles de la proteine etudiee
		chaque chaine est decomposee en residus, et chaque residu en atomes.
		Enfin, chaque atome possede des coordonnees cartesiennes dans l'espace.
		On peut acceder egalement a la liste des composants en faisant : dddd_PDB["chains"], dddd_PDB[IDchain][" reslist"], dddd_PDB[IDchain][IDres]["atomlist"].
	"""


	try :
		PDB_file = open(PDBFile, "r")
		lines = PDB_file.readlines()
	except:
		print "L'ouverture a echoue"
		sys.exit(1)

	dico_PDB = {}
	chainList = []
	rList = []

	cptAlt = False

	for line in lines:
		if line[:4:] == 'ATOM':						# si la ligne commence par 'ATOM'

			if cptAlt == False:
				alt = line[16]
				cptAlt = True

			if line[16] == alt:
				chaine = line[21]

				if chaine not in chainList:
					chainList.append(chaine)
					dico_PDB[chaine] = {}
					resList=[]

				curres = line[22:26].strip()

				if curres not in resList :
					resList.append(curres)
					dico_PDB[chaine][curres] = {}
					atomList=[]
					dico_PDB[chaine][curres]['resname'] = line[17:20].strip()

				atom = line[13:16].strip()
				if atom not in atomList:
					atomList.append(atom)
					dico_PDB[chaine][curres][atom] = {}



				dico_PDB[chaine]['reslist'] = resList
				dico_PDB[chaine][curres]['atomlist'] = atomList

				dico_PDB[chaine][curres][atom]['x'] = float(line[30:38])
				dico_PDB[chaine][curres][atom]['y'] = float(line[38:46])
				dico_PDB[chaine][curres][atom]['z'] = float(line[46:54])
				dico_PDB[chaine][curres][atom]['id'] = line[6:11].strip()




	return(dico_PDB)

dictionnaire = ParserPDB("start_prot_only.pdb")
print dictionnaire
