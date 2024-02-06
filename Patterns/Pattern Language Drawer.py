# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 11:11:33 2024

@author: cdepaor
"""

import matplotlib.pyplot as plt
import numpy as np
import image
from PIL import Image
#%% placer of blocks on the graph
def placer(word, x_pos, y_pos, image_size):
    plt.imshow(word, 
               extent=[x_pos, x_pos + image_size, y_pos + image_size/2, y_pos - image_size/2], 
               cmap='Greys', 
               origin='lower', 
               aspect='auto')
    
#%% getting the words as tiny square images 
def block_get(word):
    block = Image.open(r"{}.png". format(word)) #set working forlder to .../Moneyball/Patterns
    block = block.resize((40, 40))
    return block

#%% defining the words
arrive = block_get("Arrive 2")
arrive_up = block_get("Arrive up 2")
depart = block_get("Depart 2")
depart_down = block_get("Depart down 2")
travel = block_get("Travel 2")
separate = block_get("Separate 2")
assemble = block_get("Assemble 2")
stay = block_get("Stay 2")
entry = block_get("Entry 2")
eggsit = block_get("Exit 2")
burn = block_get("Burn 2")


#%% drawing them on a matplotlib graph
fig = plt.figure()

plt.axhline(3, 0, 1, color = "grey", linestyle = "dashed")
plt.text(13.1, 3.5, "LEO")
plt.axhline(4, 0, 1, color = "grey", linestyle = "dashed")

# plt.text(13.1, 5, "Space")

plt.axhline(6, 0, 1, color = "grey", linestyle = "dashed")
plt.text(13.1, 6.5, "NRHO")
plt.axhline(7, 0, 1, color = "grey", linestyle = "dashed")

plt.axhline(9, 0, 1, color = "grey", linestyle = "dashed")
plt.text(13.1, 9.5, "LLO")
plt.axhline(10, 0, 1, color = "grey", linestyle = "dashed")


plt.axhline(12, 0, 1, color = "grey", linestyle = "dashed")
plt.text(13.1, 12.5, "Surface")
plt.axhline(13, 0, 1, color = "grey", linestyle = "dashed")

# plt.axhline(9, 0, 1, color = "grey", linestyle = "dashed")
# plt.text(10.4, 9, "LLO")

plt.tick_params("y",colors = "white" )
xticks = np.linspace(0, 12, 13)
plt.xticks(xticks)

hfont = {"fontname":"Times New Roman"}
plt.ylabel("movement \n (change in dv)", **hfont, color = "grey", fontsize = 14)
plt.xlabel("events", **hfont, color = "grey", fontsize = 14)

# fig.figimage(im, 0, fig.bbox.ymax - height)
# origin = [80,52]
bw = 40
bh = 40

size = 1.1
#placer (word, xpos, ypos, size)    
placer(depart,      0, 0.5, size)
placer(travel,      0, 1.5, size)
placer(eggsit,      0, 1.5, size)
placer(travel,      0, 2.5, size)
placer(arrive_up,   0, 3.5, size)
placer(stay,        1, 3.5, size)
placer(depart,      2, 3.5, size)
placer(travel,      2, 4.5, size)
placer(eggsit,      2, 4.5, size)
placer(travel,      2, 5.5, size)
placer(travel,      2, 6.5, size)
placer(travel,      2, 7.5, size)
placer(travel,      2, 8.5, size)
placer(arrive_up,   2, 9.5, size)
placer(stay,        3, 9.5, size)
placer(separate,    3, 9.5, size)
placer(stay,        4, 9.5, size)
placer(stay,        5, 9.5, size)
placer(travel,      3, 10.5, size)
placer(travel,      3, 11.5, size)
placer(arrive_up,   3, 12.5, size)
placer(stay,        4, 12.5, size)
placer(depart_down, 5, 12.5, size)
placer(eggsit,      5, 12.5, size)
placer(travel,      5, 11.5, size)
placer(travel,      5, 10.5, size)
placer(separate,    5, 9.5, size)
placer(depart_down, 6, 9.5, size)
placer(eggsit,      6, 9.5, size)
placer(travel,      6, 8.5, size)
placer(travel,      6, 8.5, size)
placer(travel,      6, 7.5, size)
placer(travel,      6, 6.5, size)
placer(eggsit,      6, 4.5, size)
placer(travel,      6, 5.5, size)
placer(travel,      6, 4.5, size)
placer(travel,      6, 3.5, size)
placer(travel,      6, 2.5, size)
placer(travel,      6, 1.5, size)
placer(arrive,      6, 0.5, size)

    

plt.axis("equal")
plt.xlim(0, 13)
plt.ylim(0, 13)
