import selection.Selection;
import selection.TournamentSelection;

public class GeneticAlgorithm {
	
	private int populationSize;
	private double mutationRate;
	private double crossoverRate;
	private int elitismCount;
	
	private Selection selection;
	
	public GeneticAlgorithm(int populationSize, double mutationRate, double crossoverRate, int elitismCount) {
		this.populationSize = populationSize;
		this.mutationRate = mutationRate;
		this.crossoverRate = crossoverRate;
		this.elitismCount = elitismCount;
		this.selection = new TournamentSelection();
	}
	
	public Population initPopulation(int chromosomeLength) {
		Population population = new Population(this.populationSize, chromosomeLength);
		return population;
	}
	
	public double calcFitness(Individual individual) {
		int correctGenes = 0;
		for (int geneIndex = 0; geneIndex < individual.getChromosomeLength(); geneIndex++) {
			if (individual.getGene(geneIndex
