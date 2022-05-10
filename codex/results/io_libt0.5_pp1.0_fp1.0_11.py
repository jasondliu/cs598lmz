import io.github.mosser.arduinoml.ens.model.Brick;
import io.github.mosser.arduinoml.ens.model.CompositeState;
import io.github.mosser.arduinoml.ens.model.State;
import io.github.mosser.arduinoml.ens.model.Transition;
import io.github.mosser.arduinoml.ens.model.Variable;

public class ModelBuilder {

	private App app;
	private Map<String,Brick> bricks = new HashMap<String,Brick>();
	private Map<String,Variable> variables = new HashMap<String,Variable>();
	private Map<String,CompositeState> states = new HashMap<String,CompositeState>();
	private Map<String,Transition> transitions = new HashMap<String,Transition>();
	private List<String> errors = new ArrayList<String>();
	
	public ModelBuilder() {
		this.app = new App();
	}
	
	public void add
