#!/usr/bin/env python
#-*- coding : utf8 -*-

from math import *
import string
import re
import sys
import os


def ParserPDB(PDBfile):

    try:
		PDB_file = open(PDBfile,'r')
    except:
		print "L'ouverture a echoue"
		sys.exit(1)

    lines = PDB_file.readlines()

    dico_PDB = {}
    Flag = False

    for line in lines:

		if line[0:5] == "MODEL":
			num_model = int(string.strip(line[10:14]))
			dico_PDB[num_model] = {}
			num_model = int(num_model)
			dico_PDB[num_model]["Liste_Chaines"] = []  # numero du residu
			dico_PDB[num_model]["ResList"] = []     # noms des residus
			# le dictionnaire a la cle "Liste_Chaines" qui prend une liste

												   # Pour toutes les lignes qui commencent par ATOM (celles qui ont des atomes)
		elif line[0:4] == "ATOM":
			chain = line[24:27]
												   # on ne selectionne que les lignes qui contiennent des ATOM
			if chain not in dico_PDB[num_model]["Liste_Chaines"]:
				dico_PDB[num_model]["Liste_Chaines"].append(chain)
				dico_PDB[num_model]["ResList"].append(string.strip(line[17:20]))
				dico_PDB[num_model][chain] = {}
                                                    # pour la cle number ayant pour cle "resname"
			if dico_PDB[num_model][chain].has_key("resname") == False:
				dico_PDB[num_model][chain]["resname"] = string.strip(line[17:20])
				dico_PDB[num_model][chain]["atomlist"] = []  # a pour cle atomlist et prend une liste

			atome = string.strip(line[13:16])

			dico_PDB[num_model][chain]["atomlist"].append(atome) # ajout de l'atome a la liste

			dico_PDB[num_model][chain][atome] = {}    # cree un dictionnaire dans dico_PBD[chain][number]

			dico_PDB[num_model][chain][atome]["x"] = float(line[30:38])
			dico_PDB[num_model][chain][atome]["y"] = float(line[38:46])
			dico_PDB[num_model][chain][atome]["z"] = float(line[46:54])
			dico_PDB[num_model][chain][atome]["id"] = line[7:11].strip()


    PDB_file.close()
    return(dico_PDB)

test = ParserPDB("md_prot_only_skip100.pdb")
#~ print test



def centredemasse(dico_PDB) :

    """ Fonction qui calcule les coordonnees du centre de masse d'une proteine a partir du fichier PDB parse
        Entree : un dictionnaire (fichier PDB d'origine parse)
        Sortie : un dictionnaire contenant les coordonnees (x, y, z) du centre de masse de la proteine
    """


    dico_atomes = dict()
    dico_atomes["H"]=1
    dico_atomes["0"]=16
    dico_atomes["N"]=14
    dico_atomes["S"]=32

    dict_coord = {}

    massTot = 0


    for chain in range(0, len(dico_PDB)):
        x=y=z=0
        cpt = 0
        ResList=dico_PDB[chain]["Liste_Chaines"]
        for res in ResList:
            atomlist = dico_PDB[chain][res]["atomlist"]
            for atom in atomlist:
                #~ for key in dico_atomes.keys():
                    #~ mass = dico_atomes[key]
                x +=  dico_PDB[chain][res][atom]['x']
                y +=  dico_PDB[chain][res][atom]['y']
                z +=  dico_PDB[chain][res][atom]['z']
                #massTot += mass
                cpt+=1

        dict_coord['x']= x/cpt
        dict_coord['y']= y/cpt
        dict_coord['z']= z/cpt

    return dict_coord


dictionnaire = ParserPDB("md_prot_only_skip100.pdb")
CDM = centredemasse(dictionnaire)
#~ print dic
print CDM  


def rayon1(xA, x0, yA, y0, zA, z0):
	return sqrt((xA-x0)**2+(yA-y0)**2+(zA-z0)**2)


def gir_global(dico_PDB, CDM):
	lst_memoire=[]		

	for chain in range(0,len(dico_PDB)):
		xA=yA=zA=0
		rayon_max=0
		ResList=dico_PDB[chain]["Liste_Chaines"]
		for res in ResList:
			atomlist = dico_PDB[chain][res]["atomlist"] 
			for atom in atomlist:
					xA=dico_PDB[chain][res][atom]["x"]
					yA=dico_PDB[chain][res][atom]["y"]
					zA=dico_PDB[chain][res][atom]["z"]
					
					rayon=rayon1(xA, CDM['x'], yA, CDM['y'], zA, CDM['z'])
					if rayon>=rayon_max :
						rayon_max=rayon
						
					
		lst_memoire.append(rayon_max)
			
					
	return(lst_memoire)
	
calcul_gir = gir_global(dictionnaire, CDM)
print calcul_gir

def gir_local(dico_PDB, CDM):
	lst_memoire_loc=[]		

	for chain in range(0,len(dico_PDB)):
		xA=yA=zA=0
		rayon_max=0
		ResList=dico_PDB[chain]["Liste_Chaines"]
		for res in ResList:
			atomlist = dico_PDB[chain][res]["atomlist"] 
			for atom in atomlist:
					if atom=="CA" :
						xA=dico_PDB[chain][res][atom]["x"]
						yA=dico_PDB[chain][res][atom]["y"]
						zA=dico_PDB[chain][res][atom]["z"]
					
						rayon=rayon1(xA, CDM['x'], yA, CDM['y'], zA, CDM['z'])
						if rayon>=rayon_max :
							rayon_max=rayon
						
					
			lst_memoire_loc.append(rayon_max)
			
					
	return(lst_memoire_loc)
	
calcul_gir_loc = gir_local(dictionnaire, CDM)
print calcul_gir_loc

