import selection.Selection;
import selection.TournamentSelection;

public class GenericGA {
    private static final String GA_NAME = "Migration Based Genetic Algorithm";
    private static final String MIGRATION_BASED_GA_FOLDER = "MIGRATION_BASED_GA";
    private static final String MIGRATION_BASED_GA_FILE = "migrationBasedGa.csv";

    private Problem p;
    private Population population;
    private Selection parentSelection;
    private Crossover crossover;
    private Mutation mutation;
    private Population bestEver;
    private int populationSize;
    private int maxNoOfGens;
    private int noOfEvals;
    private int genNo;
    private int noOfMigrations;
    private int migrationFrequency;
    private int migrationSize;
    private Migration migration;
    private int noOfTrials;
    private double best;

    public GenericGA(Problem p, int populationSize, int maxNoOfGens, int migrationSize, int migrationFrequency, int noOfTrials, Migration migration) {

