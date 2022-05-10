import selector.single.SingleSelector;
import selector.single.SingleSelectorWithThreshold;
import selector.single.SingleSelectorWithThresholdAndParams;

public class SelectorTest {

	private Problem problem;
	private SolutionSet pop;
	private Population actualPop;
	private int size = 10;
	private double threshold = 0.8;
	private String name = "A";
	private Object[] params = new Object[] { "A" };

	@Before
	public void setUp() throws Exception {
		problem = new DummyProblem();
		pop = new SolutionSet(size);
		actualPop = new Population();

		for (int i = 0; i < size; i++) {
			Solution s = new Solution(problem);

			s.setObjective(0, Math.random());
			s.setObjective(1, Math.random());

			pop.add(s);
			actualPop.add(s);
		}
	}

	@Test
	public void testSingleSelectorAll() {

