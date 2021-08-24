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

relError_L2norm_CG = np.loadtxt("coarseMesh/ITHACAoutput/CGnoiseTest/relError_L2norm_mat.txt")
relError_LinfNorm_CG = np.loadtxt("coarseMesh/ITHACAoutput/CGnoiseTest/relError_LinfNorm_mat.txt")

print('L2norm CG = ',  relError_L2norm_CG.mean())
print('LinfNorm CG = ',  relError_LinfNorm_CG.mean())

f = plt.figure(2,figsize=(12,8))
plt.hist(relError_L2norm_CG, bins=50, alpha=0.5, label = r'$||\epsilon||_{L^2(\Gamma_{s_{in}})}$')
plt.hist(relError_LinfNorm_CG, bins=70, alpha=0.5, label = r'$||\epsilon||_{L^\infty(\Gamma_{s_{in}})}$')
plt.xlim(0,1)
plt.legend(fontsize=25)
plt.title("Alifanov's regularization", fontsize=25)
plt.grid()





plt.show()
