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
from ParserPDB import *


def RMSDlocal (dico_PDB):

	result_loc = []

	for chaine in dico_PDB.keys() :
		reslist = dico_PDB[chaine]["Liste_Chaines"]
		for res in reslist :
			count = somme = 0
			atomlist = dico_PDB[chaine][res]["atomlist"] # boucle sur la liste d'atomes
			for atom in atomlist :
				measure = ((dico_PDB[chaine][res][atom]["x"] - dico_PDB[0][res][atom]["x"]))**2
				+ ((dico_PDB[chaine][res][atom]["y"] - dico_PDB[0][res][atom]["y"]))**2
				+((dico_PDB[chaine][res][atom]["z"] - dico_PDB[0][res][atom]["z"]))**2
				somme+=measure
				count+=1
			RMSD=sqrt(somme/count)
			result.append(RMSD)

 	return (result_loc)

dico_PDB=ParserPDB("md_prot_only_skip100.pdb")

print RMSDlocal(dico_PDB)
