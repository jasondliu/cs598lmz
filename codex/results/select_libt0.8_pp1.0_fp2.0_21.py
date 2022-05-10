import selection.Selection;
import selection.TournamentSelection;
import selection.TournamentSelectionModified;
import selection.TournamentSelectionModifiedWithElitism;
import selection.TournamentSelectionWithElitism;
import termination.MaxIteration;
import termination.Termination;
import util.FloatVector;
import util.Random;
import crossover.SinglePointCrossover;

/**
 * This class implements a (mu+lambda)-Evolutionary algorithm. 
 * 
 * @author Le Minh Nghia, NTU-Singapore
 *
 */
public class ES {
	Population population;
	//Termination termination;
	Termination termination;
	Mutation mutation;
	Crossover crossover;
	Selection selection;
	//Evaluation evaluation;
	Evaluation evaluation;
	int esType;
	int dim;
	float lowerBound;
	float upperBound;
	float mutationRate;
	//int maxIter;
	String bestSolFileName;
	double bestFitness = -1;
	
	public ES(int _type, String _evalObj
