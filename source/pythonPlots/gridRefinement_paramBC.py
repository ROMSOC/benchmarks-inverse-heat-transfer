import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.pylab as pylab

params = {'legend.fontsize': 'x-large',
          'figure.figsize': (10, 8),
         'axes.labelsize': 'x-large',
         'axes.titlesize':'x-large',
         'xtick.labelsize':'x-large',
         'ytick.labelsize':'x-large'}
pylab.rcParams.update(params)

cellSize = np.array([0.1, 0.0667, 0.05, 0.03333, 0.025])

################################################
############## inverseProblem ##################
################################################
inverseError_L2norm = np.array([
    0.0037959628825014681171,
    0.0025852650583706449083,
    0.0038399237964380212966,
    0.0025906176199052073812,
    0.0038497870694953134976
])



inverseError_LinfNorm = np.array([
    0.015095354101075276684,
    0.011228338069575976091,
    0.017476289733333375681,
    0.012218921690098938707,
    0.018834323404958740189
])


f = plt.figure(21,figsize=(12,8))
ax1 = plt.axes(xscale='log')
ax1 = plt.axes(yscale='log')
ax1.plot(cellSize, inverseError_L2norm, 'bo', markersize=15, label=r'$||\epsilon||_{L^2(\Gamma_{s_{in}})}$')
ax1.plot(cellSize, inverseError_LinfNorm, 'kv', markersize=15, label=r'$||\epsilon||_{L^\infty(\Gamma_{s_{in}})}$')
ax1.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax1.ticklabel_format(axis="x", style="sci", scilimits=(0,0))
#plt.semilogx(gridSize,AbsError_LinfNorm, 'go')
plt.xticks(cellSize)
plt.xlabel("Cell edge length [m]", fontsize=25)
plt.legend(loc='best', fontsize=25)
plt.grid(True, which="both", ls="-")


f = plt.figure(20,figsize=(12,8))
ax1 = plt.axes(xscale='log')
ax1.plot(cellSize, inverseError_L2norm, 'bo', markersize=15, label=r'$||\epsilon||_{L^2(\Gamma_{s_{in}})}$')
ax1.plot(cellSize, inverseError_LinfNorm, 'kv', markersize=15, label=r'$||\epsilon||_{L^\infty(\Gamma_{s_{in}})}$')
ax1.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax1.ticklabel_format(axis="x", style="sci", scilimits=(0,0))
#plt.semilogx(gridSize,AbsError_LinfNorm, 'go')
#plt.xticks(cellSize)
plt.xlabel("Cell edge length [m]", fontsize=25)
plt.legend(loc='best', fontsize=25)
plt.grid()




plt.show()
