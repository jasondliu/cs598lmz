import io.github.jhg543.mellex.ASTParser.InvalidSyntaxException;
import io.github.jhg543.mellex.ASTParser.colimit;
import io.github.jhg543.mellex.ASTParser.colimit.ColimitDefinition;
import io.github.jhg543.mellex.ASTParser.colimit.TableDefinition;

public class Ast2ObjectDefineStatementProcessor implements Ast2ObjectProcessor {

	private ObjectDefinitionBuilder builder;
	private Config config;

	public Ast2ObjectDefineStatementProcessor(ObjectDefinitionBuilder builder, Config config) {
		this.builder = builder;
		this.config = config;
	}

	@Override
	public void process(Object ob) throws InvalidSyntaxException {
		assert ob instanceof define;
		define define = (define) ob;
		List<group> groups = define.getGroups();
		groups.forEach(g -> processGroup(g));
	}

	private void processGroup(group group)
