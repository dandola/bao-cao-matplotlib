import json
import numpy as np
import matplotlib.pyplot as plt
from mean import *
NoIRLM = topo_NoIRLM
NoERLM = topo_NoERLM
x=(1,5,10,15,20)
index= np.arange(2.0,15.0,3.0)
d_width= 0.6
colors=['green','red','blue','orange']
label1=['Mean NoERLM of Topology A1','Mean NoERLM of Topology A2','Mean NoERLM of Topology A3','Mean NoERLM of Topology A4']
label2=['Mean NoIRLM of Topology A1','Mean NoIRLM of Topology A2','Mean NoIRLM of Topology A3','Mean NoIRLM of Topology A4']


plt.plot(index,NoIRLM[0], marker='s',markersize=7,linewidth=2.5, color=colors[0], label=label2[0])
plt.plot(index,NoIRLM[1], marker='s',markersize=7,linewidth=2.5, color=colors[1], label=label2[1])
plt.plot(index,NoIRLM[2], marker='s',markersize=7,linewidth=2.5, color=colors[2],  label=label2[2])
plt.plot(index,NoIRLM[3], marker='s',markersize=7,linewidth=2.5, color=colors[3],label=label2[3])

plt.bar(index - 1.5*d_width, NoERLM[0],width=d_width,align='center', color=colors[0], label=label1[0])
plt.bar(index - d_width/2, NoERLM[1],width=d_width,align='center', color=colors[1], label=label1[1])
plt.bar(index + d_width/2, NoERLM[2],width=d_width,align='center', color=colors[2], label=label1[2])
plt.bar(index + 1.5*d_width, NoERLM[3], width=d_width,align='center', color=colors[3], label=label1[3])
plt.grid(True)
# plt.xlim(xmax=20)
plt.xlabel('Number of shared nodes for each rings intersection',fontsize=20)
plt.ylabel('message',fontsize=20)
plt.xticks(index ,x,fontsize=16)
plt.yticks(fontsize=16)
plt.legend()
plt.show()
