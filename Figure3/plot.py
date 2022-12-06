import numpy as np
import sys
import matplotlib.pyplot as plt

def read_dist_xvg(fname):
    dat = [[], []]
    with open(fname) as fhandle:
        for line in fhandle:
            if not (line.startswith('#') or line.startswith('@')):
                recs = line.strip().split()
                dat[0].append(float(recs[0]))
                dat[1].append(float(recs[1]))
    return dat

def read_energy_xvg(fname):
    dat = [[], []]
    with open(fname) as fhandle:
        for line in fhandle:
            if not (line.startswith('#') or line.startswith('@')):
                recs = line.strip().split()
                dat[0].append(float(recs[0]))
                dat[1].append(float(recs[1])+float(recs[2]))
    return dat

def read_98_e107_dist():
    h98_e107_dist_A = read_dist_xvg('data/wt/h98_e107_dist/h98_e107_A.xvg')
    h98_e107_dist_B = read_dist_xvg('data/wt/h98_e107_dist/h98_e107_B.xvg')
    h98_e107_dist_C = read_dist_xvg('data/wt/h98_e107_dist/h98_e107_C.xvg')
    r98_e107_dist_A = read_dist_xvg('data/h98r/r98_e107_dist/r98_e107_A.xvg')
    r98_e107_dist_B = read_dist_xvg('data/h98r/r98_e107_dist/r98_e107_B.xvg')
    r98_e107_dist_C = read_dist_xvg('data/h98r/r98_e107_dist/r98_e107_C.xvg')
    h98_e107_dist = np.concatenate((h98_e107_dist_A[1], h98_e107_dist_B[1], h98_e107_dist_C[1]), axis=None)
    r98_e107_dist = np.concatenate((r98_e107_dist_A[1], r98_e107_dist_B[1], r98_e107_dist_C[1]), axis=None)
    return (h98_e107_dist, r98_e107_dist)

def read_98_d109_dist():
    h98_d109_dist_A = read_dist_xvg('data/wt/h98_d109_dist/h98_d109_A.xvg')
    h98_d109_dist_B = read_dist_xvg('data/wt/h98_d109_dist/h98_d109_B.xvg')
    h98_d109_dist_C = read_dist_xvg('data/wt/h98_d109_dist/h98_d109_C.xvg')
    r98_d109_dist_A = read_dist_xvg('data/h98r/r98_d109_dist/r98_d109_A.xvg')
    r98_d109_dist_B = read_dist_xvg('data/h98r/r98_d109_dist/r98_d109_B.xvg')
    r98_d109_dist_C = read_dist_xvg('data/h98r/r98_d109_dist/r98_d109_C.xvg')
    h98_d109_dist = np.concatenate((h98_d109_dist_A[1], h98_d109_dist_B[1], h98_d109_dist_C[1]), axis=None)
    r98_d109_dist = np.concatenate((r98_d109_dist_A[1], r98_d109_dist_B[1], r98_d109_dist_C[1]), axis=None)
    return (h98_d109_dist, r98_d109_dist)

def read_98_e107_energy():
    h98_e107_energy_A = read_energy_xvg('data/wt/h98_e107_energy/h98_e107_A.xvg')
    h98_e107_energy_B = read_energy_xvg('data/wt/h98_e107_energy/h98_e107_B.xvg')
    h98_e107_energy_C = read_energy_xvg('data/wt/h98_e107_energy/h98_e107_C.xvg')
    r98_e107_energy_A = read_energy_xvg('data/h98r/r98_e107_energy/r98_e107_A.xvg')
    r98_e107_energy_B = read_energy_xvg('data/h98r/r98_e107_energy/r98_e107_B.xvg')
    r98_e107_energy_C = read_energy_xvg('data/h98r/r98_e107_energy/r98_e107_C.xvg')
    h98_e107_energy = np.concatenate((h98_e107_energy_A[1], h98_e107_energy_B[1], h98_e107_energy_C[1]), axis=None)
    r98_e107_energy = np.concatenate((r98_e107_energy_A[1], r98_e107_energy_B[1], r98_e107_energy_C[1]), axis=None)
    return (h98_e107_energy, r98_e107_energy)

def read_98_d109_energy():
    h98_d109_energy_A = read_energy_xvg('data/wt/h98_d109_energy/h98_d109_A.xvg')
    h98_d109_energy_B = read_energy_xvg('data/wt/h98_d109_energy/h98_d109_B.xvg')
    h98_d109_energy_C = read_energy_xvg('data/wt/h98_d109_energy/h98_d109_C.xvg')
    r98_d109_energy_A = read_energy_xvg('data/h98r/r98_d109_energy/r98_d109_A.xvg')
    r98_d109_energy_B = read_energy_xvg('data/h98r/r98_d109_energy/r98_d109_B.xvg')
    r98_d109_energy_C = read_energy_xvg('data/h98r/r98_d109_energy/r98_d109_C.xvg')
    h98_d109_energy = np.concatenate((h98_d109_energy_A[1], h98_d109_energy_B[1], h98_d109_energy_C[1]), axis=None)
    r98_d109_energy = np.concatenate((r98_d109_energy_A[1], r98_d109_energy_B[1], r98_d109_energy_C[1]), axis=None)
    return (h98_d109_energy, r98_d109_energy)

dat_98_e107_dist = read_98_e107_dist()
dat_98_d109_dist = read_98_d109_dist()
dat_98_e107_energy = read_98_e107_energy()
dat_98_d109_energy = read_98_d109_energy()

fig, ax = plt.subplots(ncols=2, nrows=2)
violin_parts = ax[0,0].violinplot(dat_98_e107_dist, positions=[0.5,1.5], showmeans=False, showmedians=True)
for n, pc in enumerate(violin_parts['bodies']):
    if n <1:
        pc.set_facecolor('red')
        pc.set_edgecolor('black')
    else:
        pc.set_facecolor('blue')
        pc.set_edgecolor('black')
ax[0,0].set_xticks([0.5,1.5])
ax[0,0].set_xticklabels(['WT','H98R'])
ax[0,0].set_ylabel("Distance (nm)")
ax[0,0].set_title("Minimun distance between H98/R98 with E107")

violin_parts = ax[0,1].violinplot(dat_98_d109_dist, positions=[0.5,1.5], showmeans=False, showmedians=True)
for n, pc in enumerate(violin_parts['bodies']):
    if n <1:
        pc.set_facecolor('red')
        pc.set_edgecolor('black')
    else:
        pc.set_facecolor('blue')
        pc.set_edgecolor('black')
ax[0,1].set_xticks([0.5,1.5])
ax[0,1].set_xticklabels(['WT','H98R'])
ax[0,1].set_ylabel("Distance (nm)")
ax[0,1].set_title("Minimun distance between H98/R98 with D109")

violin_parts = ax[1,0].violinplot(dat_98_e107_energy, positions=[0.5,1.5], showmeans=False, showmedians=True)
for n, pc in enumerate(violin_parts['bodies']):
    if n <1:
        pc.set_facecolor('red')
        pc.set_edgecolor('black')
    else:
        pc.set_facecolor('blue')
        pc.set_edgecolor('black')
ax[1,0].set_xticks([0.5,1.5])
ax[1,0].set_xticklabels(['WT','H98R'])
ax[1,0].set_ylabel("Energy (kJ/mol)")
ax[1,0].set_title("Non-bonded energy between H98/R98 with E107")

violin_parts = ax[1,1].violinplot(dat_98_d109_energy, positions=[0.5,1.5], showmeans=False, showmedians=True)
for n, pc in enumerate(violin_parts['bodies']):
    if n <1:
        pc.set_facecolor('red')
        pc.set_edgecolor('black')
    else:
        pc.set_facecolor('blue')
        pc.set_edgecolor('black')
ax[1,1].set_xticks([0.5,1.5])
ax[1,1].set_xticklabels(['WT','H98R'])
ax[1,1].set_ylabel("Energy (kJ/mol)")
ax[1,1].set_title("Non-bonded energy between H98/R98 with D109")
plt.show()

