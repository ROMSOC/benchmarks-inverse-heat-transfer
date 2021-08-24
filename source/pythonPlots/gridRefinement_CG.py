import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
from matplotlib.ticker import FormatStrFormatter

params = {'legend.fontsize': 'x-large',
          'figure.figsize': (10, 8),
         'axes.labelsize': 'x-large',
         'axes.titlesize':'x-large',
         'xtick.labelsize':'x-large',
         'ytick.labelsize':'x-large'}
pylab.rcParams.update(params)




cellSize = np.array([0.1, 0.0667, 0.05, 0.03333, 0.025, 0.02])



################################################
############## inverseProblem ##################
################################################

## Relative error of norms
inverseError_L2norm = np.array([
    0.047014507942011056485,
    0.03007098545492708358,
    0.02428983604403806007,
    0.021395297776994344485,
    0.022425771663878962814,
    0.02023264456239984993
])



inverseError_LinfNorm = np.array([
    0.15460247177687083675,
    0.087085192537911387811,
    0.06509204081616169757,
    0.056735512745029803572,
    0.060368641717922853773,
    0.054831867170013329216
])

f = plt.figure(10,figsize=(12,8))
ax1 = plt.axes(xscale='log')
ax1 = plt.axes(yscale='log')
ax1.plot(cellSize, inverseError_L2norm, 'bo', markersize=15, label=r'$||\epsilon||_{L^2(\Gamma_{s_{in}})}$')
ax1.plot(cellSize, inverseError_LinfNorm, 'kv', markersize=15, label=r'$||\epsilon||_{L^\infty(\Gamma_{s_{in}})}$')
ax1.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax1.ticklabel_format(axis="x", style="sci", scilimits=(0,0))
ax1.xaxis.set_minor_formatter(FormatStrFormatter('%1.3f'))
ax1.xaxis.set_major_formatter(FormatStrFormatter('% 1.3f'))
#plt.semilogx(gridSize,AbsError_LinfNorm, 'go')
plt.xticks(cellSize)
plt.xlabel(r"Cell edge length [$m$]", fontsize=25)
#plt.title(r"$||\epsilon|| = ||\frac{g - g_{an}}{g_{an}}||$", fontsize=25)
plt.legend(loc='best', fontsize=25)
plt.grid(True, which="both", ls="-")

## Norm of relative errors
inverseError_L2norm = np.array([
    0.045453450046719336142,
    0.028177940750564053896,
    0.022665893465868371115,
    0.020272139922173849219,
    0.021798369268752892935,
    0.019613598621504701319
])



inverseError_LinfNorm = np.array([
    0.16834491371259269199,
    0.094769180114786494284,
    0.070814418030769307744,
    0.056735512745029803572,
    0.063443099341046915729,
    0.056111634792494473334
])



f = plt.figure(20,figsize=(14,8))
ax1 = plt.axes(xscale='log')
ax1 = plt.axes(yscale='log')
ax1.plot(cellSize, inverseError_L2norm, 'bo', markersize=15, label=r'$||\epsilon||_{L^2(\Gamma_{in})}$')
ax1.plot(cellSize, inverseError_LinfNorm, 'kv', markersize=15, label=r'$||\epsilon||_{L^\infty(\Gamma_{in})}$')
ax1.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax1.ticklabel_format(axis="x", style="sci", scilimits=(0,0))
ax1.xaxis.set_minor_formatter(FormatStrFormatter('%1.3f'))
ax1.xaxis.set_major_formatter(FormatStrFormatter('% 1.3f'))
#plt.semilogx(gridSize,AbsError_LinfNorm, 'go')
plt.xticks(cellSize)
plt.xlabel(r"Cell edge length [$m$]", fontsize=20)
plt.title(r"$||\epsilon|| = \frac{||g - g_{an}||}{||g_{an}||}$", fontsize=25)
plt.legend(loc='best', fontsize=25)
plt.grid(True, which="both", ls="-")





plt.show()
