import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import pandas as pd

def read_energy_xvg(fname):
    dat = [[], []]
    with open(fname) as fhandle:
        for line in fhandle:
            if not (line.startswith('#') or line.startswith('@')):
                recs = line.strip().split()
                dat[0].append(float(recs[0]))
                dat[1].append(float(recs[1])+float(recs[2]))
    return dat

def read_hbonds_xvg(fname):
    dat = [[], []]
    with open(fname) as fhandle:
        for line in fhandle:
            if not (line.startswith('#') or line.startswith('@')):
                recs = line.strip().split()
                dat[0].append(float(recs[0]))
                dat[1].append(float(recs[1]))
    return dat

def read_94_b10b11_energy():
    e94_b10b11_energy_A = read_energy_xvg('data/wt/e94_b10b11_energy_A.xvg')
    e94_b10b11_energy_B = read_energy_xvg('data/wt/e94_b10b11_energy_B.xvg')
    e94_b10b11_energy_C = read_energy_xvg('data/wt/e94_b10b11_energy_C.xvg')
    r94_b10b11_energy_A = read_energy_xvg('data/e94r/r94_b10b11_energy_A.xvg')
    r94_b10b11_energy_B = read_energy_xvg('data/e94r/r94_b10b11_energy_B.xvg')
    r94_b10b11_energy_C = read_energy_xvg('data/e94r/r94_b10b11_energy_C.xvg')
    e94_b10b11_energy = np.concatenate((e94_b10b11_energy_A[1], e94_b10b11_energy_B[1], e94_b10b11_energy_C[1]), axis=None)
    r94_b10b11_energy = np.concatenate((r94_b10b11_energy_A[1], r94_b10b11_energy_B[1], r94_b10b11_energy_C[1]), axis=None)
    return (e94_b10b11_energy, r94_b10b11_energy)

def read_94_b10b11_hbonds():
    e94_b10b11_hbonds_A = read_hbonds_xvg('data/wt/e94_b10b11_hbonds_A.xvg')
    e94_b10b11_hbonds_B = read_hbonds_xvg('data/wt/e94_b10b11_hbonds_B.xvg')
    e94_b10b11_hbonds_C = read_hbonds_xvg('data/wt/e94_b10b11_hbonds_C.xvg')
    r94_b10b11_hbonds_A = read_hbonds_xvg('data/e94r/r94_b10b11_hbonds_A.xvg')
    r94_b10b11_hbonds_B = read_hbonds_xvg('data/e94r/r94_b10b11_hbonds_B.xvg')
    r94_b10b11_hbonds_C = read_hbonds_xvg('data/e94r/r94_b10b11_hbonds_C.xvg')
    e94_b10b11_hbonds = np.concatenate((e94_b10b11_hbonds_A[1], e94_b10b11_hbonds_B[1], e94_b10b11_hbonds_C[1]), axis=None)
    r94_b10b11_hbonds = np.concatenate((r94_b10b11_hbonds_A[1], r94_b10b11_hbonds_B[1], r94_b10b11_hbonds_C[1]), axis=None)
    return (e94_b10b11_hbonds, r94_b10b11_hbonds)

dat_94_b10b11_energy = read_94_b10b11_energy()
dat_94_b10b11_hbonds = read_94_b10b11_hbonds()

fig, ax = plt.subplots()
violin_parts = ax.violinplot(dat_94_b10b11_energy, positions=[0.5,1.5], showmeans=False, showmedians=True)
for n, pc in enumerate(violin_parts['bodies']):
    if n <1:
        pc.set_facecolor('red')
        pc.set_edgecolor('black')
    else:
        pc.set_facecolor('blue')
        pc.set_edgecolor('black')
ax.set_xticks([0.5,1.5])
ax.set_xticklabels(['WT','e94r'])
ax.set_ylabel("Energy (kJ/mol)")
ax.set_title("Non-bonded energy between H98/R98 with b10-b11 loop")
plt.show()


data = pd.DataFrame({"hbonds": np.concatenate(dat_94_b10b11_hbonds, axis=None), "Mutant": ["WT"]*len(dat_94_b10b11_hbonds[0]) + ["E94R"]*len(dat_94_b10b11_hbonds[1])})
sns.set_style('whitegrid')
sns.displot(data=data, x="hbonds", hue="Mutant", multiple="dodge", stat="probability")
plt.xticks([1, 2, 3])
plt.xlim(0.5,3.5)
plt.ylim(0.0,0.06)
plt.show()
