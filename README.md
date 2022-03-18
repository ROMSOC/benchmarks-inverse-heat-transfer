<img src="resources/romsoclogo-logo.png" alt="EU Flag"  width="150"/>

# Benchmarls in inverse heat transfer 

## Boundary heat flux estimation in continuous casting molds
Benchmak case for the boundary heat flux estimation in a continuous casting mold given pointwise temeprature measurements

<a href="https://doi.org/10.5281/zenodo.5242918"><img src="https://zenodo.org/badge/DOI/10.5281/zenodo.5242918.svg" alt="DOI"></a>

The repository contains scripts for generating the relevant meshes and solving the inverse problem of estimating the boundary ehat flux in a continuous casting mold. The considered domain is a simplification of a continuous casting mold.

The motivation and technical details of the source code are highlighted in the paper
Morelli, UE, Barral, P, Quintela, P, Rozza, G, Stabile, G. <i>"A numerical approach for heat flux estimation in thin slabs continuous casting molds using data assimilation"</i>. Int J Numer Methods Eng. 2021; 122: 4541– 4574. https://doi.org/10.1002/nme.6713

### DESCRIPTION

This script relyes on the C++ libraries [OpenFOAM](https://www.openfoam.com/) and [ITHACA-FV](https://mathlab.sissa.it/ithaca-fv).

- To generate the mesh, run the OpenFOAM command `blockMesh`
- In the `thermocouplesDict`, you can select the position of the thermocouples
- Before running the case, go to the `ITHACAdict` file to select the maximum number of iterations, `cgIterMax`, the absolute, `Jtolerance`, and relative,
`JrelativeTolerance`, tolerance for the Alifanov’s regularization algorithm. While, for the parameterization of the BC method, the user can select the shape parameter for the radial basis functions used for the parameterization, `rbfShapePar`. In this same file, select the test you want to run by setting the related flag to 1.
- Run the script by typing the command `IHTP01inverseLaplacian`.
- The outputs are all saved into the directory `ITHACAoutputs` in different subdirectories according to the different tests.

### POSTPROCESSING
The output of the simulations are all saved into the `ITHACAoutputs` folder. For the post processing of the results, several python codes are available at the directory `pythonPlots`. To obtain the post processing plot, the user must run the command `python required-plots.py` where required-plots should be selected by the ones available in the folder, e.g. `python CGconvergence.py` to see the convergence of the Alifanov’s regularization and the behaviour of the error with the iterations.

### RUN JUPYTER NOTEBOOKS
The entire benchmark repository can be executed in a provided Docker container where a full installation of OpenFOAM and ITHACA-FV is available. Once you have clone or downloaded this repository, to build the container just type
```bash
docker build -t benchmarks-inverse-heat-transfer . 
```
and for running it locally:
```bash
docker run -u 0 -it --rm -p 8888:8888 benchmarks-inverse-heat-transfer jupyter-lab --ip=0.0.0.0 --port=8888 --allow-root
```

Alternatively, user-friendly Jupyter Notebooks could be used to run different benchmarks on the cloud. For instance, the benchmark (part of the ITHACA-FV tutorials) is available at:
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ROMSOC/benchmarks-inverse-heat-transfer/HEAD). Please, notice that mybinder cloud computations are limited to 2GB of RAM memory and the current setting of this benchamark with the mesh included in this repository requires around 8GB (it is recommended use this notebook for pre- and post-processing purposes when running large OpenFOAM simulations).

<hr style="border:1px" > 

### DISCLAIMER

In downloading this SOFTWARE you are deemed to have read and agreed to the following terms:

This SOFTWARE has been designed with an exclusive focus on civil applications. It is not to be used
for any illegal, deceptive, misleading or unethical purpose or in any military applications. This includes ANY APPLICATION WHERE THE USE OF THE SOFTWARE MAY RESULT IN DEATH, PERSONAL INJURY OR SEVERE PHYSICAL OR ENVIRONMENTAL DAMAGE. Any redistribution of the software must retain this disclaimer. BY INSTALLING, COPYING, OR OTHERWISE USING THE SOFTWARE, YOU AGREE TO THE TERMS ABOVE. IF YOU DO NOT AGREE TO THESE TERMS, DO NOT INSTALL OR USE THE SOFTWARE

<hr style="border:1px" > 

### ACKNOWLEDGEMENTS

<img src="resources/EU_Flag.png" alt="EU Flag"  width="75" height="50" />

The ROMSOC project has received funding from the European Union’s Horizon 2020 research and innovation programme under the Marie Skłodowska-Curie Grant Agreement No. 765374. This repository reflects the views of the author(s) and does not necessarily reflect the views or policy of the European Commission. The REA cannot be held responsible for any use that may be made of the information this repository contains.

<hr style="border:1px">

