# SPDX-License-Identifier: LGPL-3.0-or-later

FROM ithacafv/ithacafv:manifest-amd64
ENV LAST_UPDATED=2022-03-01

USER root
WORKDIR /tmp

# Install pip3 from system packages
RUN apt-get update --yes && \
  apt-get install --yes --no-install-recommends python3-pip 

ARG NB_USER="ithacafv"
ARG NB_UID="1000"
ARG NB_GID="100"

# Fix DL4006
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

# Install JupyterLab
USER root

RUN chmod 777 /tmp        && \
    DEBIAN_FRONTEND="noninteractive" && \
    pip3 install --upgrade --no-cache-dir \
      jupyterlab                    \
      jupytext                      \
      jupyter-book                  \
      ghp-import

# allow jupyterlab for ipyvtk
ENV JUPYTER_ENABLE_LAB=yes
ENV PYVISTA_USE_IPYVTK=true

# Install basic Python packages
USER root
RUN apt-get update --yes
RUN apt-get install --yes --no-install-recommends python3-dev && \
    pip3 -q install numpy scipy matplotlib 

# Install locales
RUN apt-get install -yq --no-install-recommends locales-all && locale

# cleanup
RUN apt-get --yes clean          && \
    apt-get --yes autoremove     && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* 

# Configure environment
ENV SHELL=/bin/bash \
    NB_USER="${NB_USER}" \
    NB_UID=${NB_UID} \
    NB_GID=${NB_GID} \
    LC_ALL=en_US.UTF-8 \
    LANG=en_US.UTF-8 \
    LANGUAGE=en_US.UTF-8 \
    HOME="/home/${NB_USER}" \
    HOSTNAME=jupyter \
    ADIOS2_ARCH_PATH="/usr/lib/openfoam/openfoam2106/ThirdParty/platforms/linux64Gcc/ADIOS2-2.6.0" \
    BOOST_ARCH_PATH="/usr/lib/openfoam/openfoam2106/ThirdParty/platforms/linux64Gcc/boost-system" \
    CGAL_ARCH_PATH="/usr/lib/openfoam/openfoam2106/ThirdParty/platforms/linux64Gcc/cgal-system" \
    FFTW_ARCH_PATH="/usr/lib/openfoam/openfoam2106/ThirdParty/platforms/linux64Gcc/fftw-system" \
    FOAM_API="2106" \
    FOAM_APP="/usr/lib/openfoam/openfoam2106/applications" \
    FOAM_APPBIN="/usr/lib/openfoam/openfoam2106/platforms/linux64GccDPInt32Opt/bin" \
    FOAM_ETC="/usr/lib/openfoam/openfoam2106/etc" \
    FOAM_LIBBIN="/usr/lib/openfoam/openfoam2106/platforms/linux64GccDPInt32Opt/lib" \
    FOAM_MPI="sys-openmpi" \
    FOAM_RUN="/home/ithacafv/OpenFOAM/ithacafv-v2106/run" \
    FOAM_SITE_APPBIN="/usr/lib/openfoam/openfoam2106/site/2106/platforms/linux64GccDPInt32Opt/bin" \
    FOAM_SITE_LIBBIN="/usr/lib/openfoam/openfoam2106/site/2106/platforms/linux64GccDPInt32Opt/lib" \
    FOAM_SOLVERS="/usr/lib/openfoam/openfoam2106/applications/solvers" \
    FOAM_SRC="/usr/lib/openfoam/openfoam2106/src" \
    FOAM_TUTORIALS="/usr/lib/openfoam/openfoam2106/tutorials" \
    FOAM_USER_APPBIN="/home/ithacafv/OpenFOAM/ithacafv-v2106/platforms/linux64GccDPInt32Opt/bin" \
    FOAM_USER_LIBBIN="/home/ithacafv/OpenFOAM/ithacafv-v2106/platforms/linux64GccDPInt32Opt/lib" \
    FOAM_UTILITIES="/usr/lib/openfoam/openfoam2106/applications/utilities" \
    LD_LIBRARY_PATH="/usr/lib/openfoam/openfoam2106/platforms/linux64GccDPInt32Opt/lib/sys-openmpi:/usr/lib/x86_64-linux-gnu/openmpi/lib:/home/ithacafv/OpenFOAM/ithacafv-v2106/platforms/linux64GccDPInt32Opt/lib:/usr/lib/openfoam/openfoam2106/site/2106/platforms/linux64GccDPInt32Opt/lib:/usr/lib/openfoam/openfoam2106/platforms/linux64GccDPInt32Opt/lib:/usr/lib/openfoam/openfoam2106/platforms/linux64GccDPInt32Opt/lib/dummy" \
    LIB_ITHACA="/usr/lib/ITHACA-FV" \
    LIB_ITHACA_SRC="/usr/lib/ITHACA-FV/src" \
    MPI_ARCH_PATH="/usr/lib/x86_64-linux-gnu/openmpi" \
    OMPI_MCA_btl_base_warn_component_unused="0" \
    OMPI_MCA_btl_vader_single_copy_mechanism="none" \
    PATH="/home/ithacafv/OpenFOAM/ithacafv-v2106/platforms/linux64GccDPInt32Opt/bin:/usr/lib/openfoam/openfoam2106/site/2106/platforms/linux64GccDPInt32Opt/bin:/usr/lib/openfoam/openfoam2106/platforms/linux64GccDPInt32Opt/bin:/usr/lib/openfoam/openfoam2106/bin:/usr/lib/openfoam/openfoam2106/wmake:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/lib/ITHACA-FV/bin" \
    WM_ARCH="linux64" \
    WM_COMPILER="Gcc" \
    WM_COMPILER_LIB_ARCH="64" \
    WM_COMPILER_TYPE="system" \
    WM_COMPILE_OPTION="Opt" \
    WM_DIR="/usr/lib/openfoam/openfoam2106/wmake" \
    WM_LABEL_OPTION="Int32" \
    WM_LABEL_SIZE="32" \
    WM_MPLIB="SYSTEMOPENMPI" \
    WM_OPTIONS="linux64GccDPInt32Opt" \
    WM_PRECISION_OPTION="DP" \
    WM_PROJECT="OpenFOAM" \
    WM_PROJECT_DIR="/usr/lib/openfoam/openfoam2106" \
    WM_PROJECT_USER_DIR="/home/ithacafv/OpenFOAM/ithacafv-v2106" \
    WM_PROJECT_VERSION="v2106" \
    WM_THIRD_PARTY_DIR="/usr/lib/openfoam/openfoam2106/ThirdParty"

# Make sure the contents of our repo are in ${HOME}
COPY . ${HOME}
COPY source/Benchmark.ipynb /usr/lib/ITHACA-FV/tutorials/inverseHeatTransfer/IHTP01inverseLaplacian/

# Switch back to jovyan to avoid accidental container runs as root
USER $USER
WORKDIR /usr/lib/ITHACA-FV/tutorials/inverseHeatTransfer/IHTP01inverseLaplacian/
ENTRYPOINT []
