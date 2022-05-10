import selection.Selection;
import selection.RouletteWheelSelection;

public class Algorithm_05 extends Algorithm {
    private int tournamentSize;
    private Selection selection;
    private Reproduction reproduction;
    private Replacement replacement;

    public Algorithm_05(int populationSize, double crossoverProbability, double mutationProbability, int tournamentSize, Selection selection, Reproduction reproduction, Replacement replacement) {
        super(populationSize, crossoverProbability, mutationProbability);
        this.tournamentSize = tournamentSize;
        this.selection = selection;
        this.reproduction = reproduction;
        this.replacement = replacement;
    }

    @Override
    protected Population nextPopulation() {
        Population newPopulation = new Population();

        while (newPopulation.size() != getPopulation().size()) {
            Population tempPopulation = new Population();
            for (int i = 0; i < tournamentSize; i++) {
                tempPopulation.addIndividual(getPopulation().getIndividual(RandomUtils.nextInt(0, getPopulation().size())));
            }
            if (selection instanceof RouletteWheel
