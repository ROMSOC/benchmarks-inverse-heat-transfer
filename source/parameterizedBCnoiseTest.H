Info << endl;
Info << "*********************************************************" << endl;
Info << "Testing parameterized BC inverse solver with NOISY data" <<
     endl;
word outputFolder = "./ITHACAoutput/parameterizedBCnoiseTest/";
volScalarField gTrueField = example_paramBC.list2Field(example_paramBC.gTrue);
ITHACAstream::exportSolution(gTrueField,
                             "1", outputFolder,
                             "gTrue");
List<List<scalar>> heatFluxWeights;
Eigen::VectorXd residualNorms;
scalar innerField = 1.0;
example_paramBC.set_gParametrized("rbf", rbfShapePar);
example_paramBC.parameterizedBCoffline();
List<word> linSys_solvers;
linSys_solvers.resize(1);
//linSys_solvers[0] = "fullPivLU";
//linSys_solvers[1] = "jacobiSvd";
//linSys_solvers[2] = "householderQr";
//linSys_solvers[3] = "ldlt";
linSys_solvers[0] = "TSVD";
Info << "Introducing error in the measurements" << endl;
Info << "Performing " << Ntests << " tests." << endl;
residualNorms.resize(Ntests* linSys_solvers.size());
Eigen::VectorXd TmeasOrig = example_paramBC.Tmeas;
auto density = std::make_shared<muq::Modeling::Gaussian>(Eigen::VectorXd::Zero(
                   1), Eigen::VectorXd::Ones(1));

for (label i = 0; i < Ntests; i++)
{
    Info << "Test " << i << endl;
    example_paramBC.addNoise(noiseLevel);
    List<List<scalar>> heatFluxWeights_err = heatFluxWeights;
    List<scalar> solutionNorms;
    forAll(linSys_solvers, solverI)
    {
        Info << "Solver " << linSys_solvers[solverI] << endl;
        example_paramBC.parameterizedBC(linSys_solvers[solverI], 3);
        Info << endl;
        volScalarField gParametrizedField = example_paramBC.list2Field(
                                                example_paramBC.g);
        ITHACAstream::exportSolution(gParametrizedField,
                                     std::to_string(i * linSys_solvers.size() + solverI + 1),
                                     outputFolder,
                                     "gParametrized");
        ITHACAstream::exportSolution(example_paramBC.T,
                                     std::to_string(i * linSys_solvers.size() + solverI + 1),
                                     outputFolder,
                                     "T");
        residualNorms(i * linSys_solvers.size() + solverI) = Foam::sqrt(
                    example_paramBC.residual.squaredNorm());
    }
    example_paramBC.Tmeas = TmeasOrig;
}

example_paramBC.postProcess(outputFolder, "gParametrized", innerField);
Info << "*********************************************************" << endl;
Info << endl;
