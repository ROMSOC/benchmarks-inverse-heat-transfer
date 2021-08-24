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

relError_L2norm_paramBC = np.loadtxt("coarseMesh/ITHACAoutput/parameterizedBCnoiseTest/relError_L2norm_mat.txt")
relError_LinfNorm_paramBC = np.loadtxt("coarseMesh/ITHACAoutput/parameterizedBCnoiseTest/relError_LinfNorm_mat.txt")


print('L2norm LDLT = ',  relError_L2norm_paramBC.mean())
print('LinfNorm LDLT = ',  relError_LinfNorm_paramBC.mean())

f = plt.figure(3,figsize=(12,8))
plt.hist(relError_L2norm_paramBC,bins=20, alpha=0.5, label = r'$||\epsilon||_{L^2(\Gamma_{s_{in}})}$')
plt.hist(relError_LinfNorm_paramBC, bins=20, alpha=0.5, label = r'$||\epsilon||_{L^\infty(\Gamma_{s_{in}})}$')
plt.xlim(left=0)
plt.title(r"TSVD, $\alpha_{TSVD}$ = 3", fontsize=25)
plt.legend(fontsize=25)
plt.grid()


##paramBC delivers a vector that has solutions for different solvers in series
#relError_L2norm_LU = relError_L2norm_paramBC[0::4]
#relError_L2norm_JacobiSVD = relError_L2norm_paramBC[1::4]
#relError_L2norm_QR = relError_L2norm_paramBC[2::4]
#relError_L2norm_LDLT = relError_L2norm_paramBC[3::4]
#
#relError_LinfNorm_LU = relError_LinfNorm_paramBC[0::4]
#relError_LinfNorm_JacobiSVD = relError_LinfNorm_paramBC[1::4]
#relError_LinfNorm_QR = relError_LinfNorm_paramBC[2::4]
#relError_LinfNorm_LDLT = relError_LinfNorm_paramBC[3::4]
#
#print('L2norm LU = ',  relError_L2norm_LU.mean())
#print('LinfNorm LU = ',  relError_LinfNorm_LU.mean())
#
#print('L2norm JacobiSVD = ',  relError_L2norm_JacobiSVD.mean())
#print('LinfNorm JacobiSVD = ',  relError_LinfNorm_JacobiSVD.mean())
#
#print('L2norm QR = ',  relError_L2norm_QR.mean())
#print('LinfNorm QR = ',  relError_LinfNorm_QR.mean())
#
#print('L2norm LDLT = ',  relError_L2norm_LDLT.mean())
#print('LinfNorm LDLT = ',  relError_LinfNorm_LDLT.mean())
#
#f = plt.figure(3,figsize=(12,8))
#plt.hist(relError_L2norm_LU,bins=20, alpha=0.5, label = r'$||\epsilon||_{L^2(\Gamma_{s_{in}})}$')
#plt.hist(relError_LinfNorm_LU, bins=20, alpha=0.5, label = r'$||\epsilon||_{L^\infty(\Gamma_{s_{in}})}$')
#plt.xlim(left=0)
#plt.title("LU", fontsize=25)
#plt.legend(fontsize=25)
#plt.grid()
#
#f = plt.figure(4,figsize=(12,8))
#plt.hist(relError_L2norm_JacobiSVD, bins=20, alpha=0.5, label = r'$||\epsilon||_{L^2(\Gamma_{s_{in}})}$')
#plt.hist(relError_LinfNorm_JacobiSVD, bins=20, alpha=0.5, label = r'$||\epsilon||_{L^\infty(\Gamma_{s_{in}})}$')
#plt.xlim(left=0)
#plt.title("JacobiSVD", fontsize=25)
#plt.legend(fontsize=25)
#plt.grid()
#
#
#f = plt.figure(5,figsize=(12,8))
#plt.hist(relError_L2norm_QR, bins=20, alpha=0.5, label = r'$||\epsilon||_{L^2(\Gamma_{s_{in}})}$')
#plt.hist(relError_LinfNorm_QR, bins=20, alpha=0.5, label = r'$||\epsilon||_{L^\infty(\Gamma_{s_{in}})}$')
#plt.xlim(left=0)
#plt.title("QR", fontsize=25)
#plt.legend(fontsize=25)
#plt.grid()
#
#
#f = plt.figure(6,figsize=(12,8))
#plt.hist(relError_L2norm_LDLT, bins=20, alpha=0.5, label = r'$||\epsilon||_{L^2(\Gamma_{s_{in}})}$')
#plt.hist(relError_LinfNorm_LDLT, bins=20, alpha=0.5, label = r'$||\epsilon||_{L^\infty(\Gamma_{s_{in}})}$')
#plt.xlim(left=0)
#plt.title("LDLT", fontsize=25)
#plt.legend(fontsize=25)
#plt.grid()










plt.show()
