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

relError_L2norm = np.loadtxt("coarseMesh/ITHACAoutput/parameterizedBCnoiseTest_TSVD/relError_L2norm_mat.txt")
relError_LinfNorm = np.loadtxt("coarseMesh/ITHACAoutput/parameterizedBCnoiseTest_TSVD/relError_LinfNorm_mat.txt")

#Have a look at the vector TSVDtruc in analyticalBenchmark.C 
TSVDtruc = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,14, 15])

relErr_L2norm = np.empty([len(TSVDtruc)])
relErr_L2normMin = np.empty([len(TSVDtruc)])
relErr_L2normMax = np.empty([len(TSVDtruc)])
relErr_LinfNorm = np.empty([len(TSVDtruc)])
relErr_LinfNormMin = np.empty([len(TSVDtruc)])
relErr_LinfNormMax = np.empty([len(TSVDtruc)])

for i in range(len(TSVDtruc)):
    vec = relError_L2norm[i::len(TSVDtruc)]
    relErr_L2norm[i] = vec.mean() 
    relErr_L2normMin[i] = np.quantile(vec, 0.1) 
    relErr_L2normMax[i] = np.quantile(vec, 0.9) 
    vec = relError_LinfNorm[i::len(TSVDtruc)]
    relErr_LinfNorm[i] = vec.mean() 
    relErr_LinfNormMin[i] = np.quantile(vec, 0.1) 
    relErr_LinfNormMax[i] = np.quantile(vec, 0.9) 

print relErr_L2norm
f = plt.figure(3,figsize=(12,8))
plt.errorbar(TSVDtruc, relErr_L2norm, yerr=[relErr_L2norm - relErr_L2normMin, relErr_L2normMax - relErr_L2norm], markersize=15,fmt='bo', capsize=12, label = r'$||\epsilon||_{L^2(\Gamma_{s_{in}})}$')
plt.errorbar(TSVDtruc, relErr_LinfNorm, yerr=[relErr_LinfNorm - relErr_LinfNormMin, relErr_LinfNormMax - relErr_LinfNorm], markersize=15,fmt='kv', capsize=12, label = r'$||\epsilon||_{L^\infty(\Gamma_{s_{in}})}$')
plt.xlabel(r'$\alpha_{TSVD}$', fontsize=25)
plt.title(r'Noise standard dev. = $0.1$', fontsize=25)
plt.yscale('log')
plt.grid()
plt.legend(fontsize=25)
plt.show()

##paramBC delivers a vector that has solutions for different solvers in series
#relError_L2norm_LU = relError_L2norm[0::4]
#relError_L2norm_JacobiSVD = relError_L2norm[1::4]
#relError_L2norm_QR = relError_L2norm[2::4]
#relError_L2norm_LDLT = relError_L2norm[3::4]
#
#relError_LinfNorm_LU = relError_LinfNorm[0::4]
#relError_LinfNorm_JacobiSVD = relError_LinfNorm[1::4]
#relError_LinfNorm_QR = relError_LinfNorm[2::4]
#relError_LinfNorm_LDLT = relError_LinfNorm[3::4]
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
#plt.hist(relError_L2norm_LU,bins=50, alpha=0.5, label = r'$||\epsilon||_{L^2(\Gamma_{s_{in}})}$')
#plt.hist(relError_LinfNorm_LU, bins=50, alpha=0.5, label = r'$||\epsilon||_{L^\infty(\Gamma_{s_{in}})}$')
#plt.xlim(left=0)
#plt.title("LU", fontsize=25)
#plt.legend(fontsize=25)
#plt.grid()
#
#f = plt.figure(4,figsize=(12,8))
#plt.hist(relError_L2norm_JacobiSVD, bins=50, alpha=0.5, label = r'$||\epsilon||_{L^2(\Gamma_{s_{in}})}$')
#plt.hist(relError_LinfNorm_JacobiSVD, bins=50, alpha=0.5, label = r'$||\epsilon||_{L^\infty(\Gamma_{s_{in}})}$')
#plt.xlim(left=0)
#plt.title("JacobiSVD", fontsize=25)
#plt.legend(fontsize=25)
#plt.grid()
#
#
#f = plt.figure(5,figsize=(12,8))
#plt.hist(relError_L2norm_QR, bins=50, alpha=0.5, label = r'$||\epsilon||_{L^2(\Gamma_{s_{in}})}$')
#plt.hist(relError_LinfNorm_QR, bins=50, alpha=0.5, label = r'$||\epsilon||_{L^\infty(\Gamma_{s_{in}})}$')
#plt.xlim(left=0)
#plt.title("QR", fontsize=25)
#plt.legend(fontsize=25)
#plt.grid()
#
#
#f = plt.figure(6,figsize=(12,8))
#plt.hist(relError_L2norm_LDLT, bins=50, alpha=0.5, label = r'$||\epsilon||_{L^2(\Gamma_{s_{in}})}$')
#plt.hist(relError_LinfNorm_LDLT, bins=50, alpha=0.5, label = r'$||\epsilon||_{L^\infty(\Gamma_{s_{in}})}$')
#plt.xlim(left=0)
#plt.title("LDLT", fontsize=25)
#plt.legend(fontsize=25)
#plt.grid()
#
#
#
#
#
#
#
#
#
#
#plt.show()
