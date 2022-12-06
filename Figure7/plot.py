import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import sys

def read_xvg(fname):
    dat = [[], []]
    with open(fname) as fhandle:
        for line in fhandle:
            if not (line.startswith('#') or line.startswith('@')):
                recs = line.strip().split()
                dat[0].append(float(recs[0]))
                dat[1].append(float(recs[1]))
    return dat

### Figure 7D ###
wt_A = read_xvg('data/wt/e250_d207_dist_A.xvg')
wt_B = read_xvg('data/wt/e250_d207_dist_B.xvg')
wt_C = read_xvg('data/wt/e250_d207_dist_C.xvg')
e250r_A = read_xvg('data/e250r/r250_d207_dist_A.xvg')
e250r_B = read_xvg('data/e250r/r250_d207_dist_B.xvg')
e250r_C = read_xvg('data/e250r/r250_d207_dist_C.xvg')

fig, ax = plt.subplots()
wt = np.concatenate((wt_A[1], wt_B[1], wt_C[1]), axis=None)
e250r = np.concatenate((e250r_A[1], e250r_B[1], e250r_C[1]), axis=None)
violin_parts = ax.violinplot((wt, e250r), positions=[0.5,1.5], showmeans=False, showmedians=True)
for n, pc in enumerate(violin_parts['bodies']):
    if n <1:
        pc.set_facecolor('red')
        pc.set_edgecolor('black')
    else:
        pc.set_facecolor('blue')
        pc.set_edgecolor('black')
ax.set_xticks([0.5,1.5])
#ax.set_yticks([3,6,9,12,15,18])
#ax.set_ylim([0,22])
ax.set_xticklabels(['WT','E250R'])
ax.set_ylabel("Distance (nm)")
ax.set_title("Minimun distance between E250/R250 with D297")
plt.show()

### Figure 7E ###
wt_A = read_xvg('data/wt/e250_d207_hbonds_A.xvg')
wt_B = read_xvg('data/wt/e250_d207_hbonds_B.xvg')
wt_C = read_xvg('data/wt/e250_d207_hbonds_C.xvg')
e250r_A = read_xvg('data/e250r/r250_d207_hbonds_A.xvg')
e250r_B = read_xvg('data/e250r/r250_d207_hbonds_B.xvg')
e250r_C = read_xvg('data/e250r/r250_d207_hbonds_C.xvg')

wt_v = list(map(np.mean,(wt_A[1], wt_B[1], wt_C[1])))
wt_mean = np.mean(wt_v)
e250r_v = list(map(np.mean,(e250r_A[1], e250r_B[1], e250r_C[1])))
e250r_mean = np.mean(e250r_v)

fig, ax = plt.subplots()
ax.bar([1, 2], [wt_mean, e250r_mean])
ax.set_ylabel("Frequency (%)")
ax.set_xlim(0.5,2.5)
plt.show()

