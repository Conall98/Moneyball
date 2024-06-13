# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 13:09:42 2024

@author: cdepaor
"""
#%%
import matplotlib.pyplot as plt
import numpy as np
import image
from PIL import Image
#%% class for the vocabulary
class word:
    def __init__(self, name, indir, outdir):
        self.name = name #[string]
        self.indir = indir #[1, 2, 3, 4]
        self.outdir = outdir #[1, 2, 3, 4]
        self.photo = Image.open("{}.png".format(name)) #[jpg]
        
#%% defining the words / blocks       
arrive_down = word("Arrive", 1, 2)
arrive_up = word("Arrive up", 3, 2)
depart_up = word("Depart", 4, 1)
depart_down = word("Depart down", 4, 3)
travel_up = word("Travel", 3, 1)
travel_down = word("Travel", 1, 3)
eggsit_up = word("Exit", 1, 3)
eggsit_down = word("Exit", 3, 1)
stay = word("Stay", 4, 2)
burn_up = word("Burn", 3, 1)
burn_down = word("Burn", 1, 3)
assemble = word("Assemble", 3, 2)
separate = word("Assemble", 3, 2)

#%% defining the grammar
def cont_check(block1, block2):
    indir1 = block1.indir
    outdir1 = block1.outdir
    indir2 = block2.indir
    outdir2 = block2.outdir
    
    
    