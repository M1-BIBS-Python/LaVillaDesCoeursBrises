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

def centredemasse(dico_PDB) :

    """ Fonction qui calcule les coordonnees du centre de masse d'une proteine a partir du fichier PDB parse
        Entree : un dictionnaire (fichier PDB d'origine parse)
        Sortie : un dictionnaire contenant les coordonnees (x, y, z) du centre de masse de la proteine
    """
    dict_coord={}

    for chain in range(0, len(dico_PDB)):
        x=y=z=0
        cpt = 0
        ResList=dico_PDB[chain]["Liste_Chaines"]
        for res in ResList:
            atomlist = dico_PDB[chain][res]["atomlist"]
            for atom in atomlist:
                x +=  dico_PDB[chain][res][atom]['x']
                y +=  dico_PDB[chain][res][atom]['y']
                z +=  dico_PDB[chain][res][atom]['z']
                cpt+=1

        dict_coord['x']= x/cpt
        dict_coord['y']= y/cpt
        dict_coord['z']= z/cpt

        return dict_coord

dictionnaire = ParserPDB("md_prot_only_skip100.pdb")
test = centredemasse(dictionnaire)
print test
