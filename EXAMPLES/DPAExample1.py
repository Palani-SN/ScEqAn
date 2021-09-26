from ScEqAn.Analysis import DynamicProgramAnalysis

OBJ = DynamicProgramAnalysis("InputFiles/Input.txt", "OutputFiles/Output.log");

# For printing the results to console, set Debug = True
OBJ.Run(Debug = True);

# For printing the results to console, set Debug = False
OBJ.Run(Debug = False);