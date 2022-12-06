import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def read_xvg(fname):
    dat = [[], []]
    with open(fname) as fhandle:
        for line in fhandle:
            if not (line.startswith('#') or line.startswith('@')):
                recs = line.strip().split()
                dat[0].append(float(recs[0]))
                dat[1].append(float(recs[1]))
    return dat

wt_A = read_xvg('data/wt/d91_lipids_hbonds_A.xvg')
wt_B = read_xvg('data/wt/d91_lipids_hbonds_B.xvg')
wt_C = read_xvg('data/wt/d91_lipids_hbonds_C.xvg')

d91r_A = read_xvg('data/d91r/r91_lipids_hbonds_A.xvg')
d91r_B = read_xvg('data/d91r/r91_lipids_hbonds_B.xvg')
d91r_C = read_xvg('data/d91r/r91_lipids_hbonds_C.xvg')

wt = np.concatenate((wt_A[1], wt_B[1], wt_C[1]), axis=None)
d91r = np.concatenate((d91r_A[1], d91r_B[1], d91r_C[1]), axis=None)
data = pd.DataFrame({"hbonds": np.concatenate((wt,d91r), axis=None), "Mutant": ["WT"]*len(wt) + ["d91r"]*len(d91r)})
sns.set_style('whitegrid')
ax = sns.displot(data=data, x="hbonds", hue="Mutant", multiple="dodge", stat="probability")
plt.xticks([0, 1, 2, 3, 4, 5])
plt.ylim(0.0,0.25)
plt.show()
