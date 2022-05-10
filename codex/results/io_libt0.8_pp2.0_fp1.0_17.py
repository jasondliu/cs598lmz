import io.vertigo.quarto.publisher.impl.merger.script.ScriptExpressionLanguage;
import io.vertigo.quarto.publisher.impl.merger.script.ScriptExpressionLanguageExecutor;
import io.vertigo.quarto.publisher.impl.merger.script.rhino.RhinoEngine;
import io.vertigo.quarto.publisher.impl.merger.script.rhino.RhinoEngineProvider;
import io.vertigo.quarto.publisher.impl.merger.script.rhino.RhinoScript;

/**
 * Implémentation de l'interface d'accès à l'expression language.
 *
 * @author npiedeloup
 * @version $Id: ScriptExpressionLanguageExecutorImpl.java,v 1.2 2011/08/02 15:24:51 npiedeloup Exp $
 */
public final class ScriptExpressionLanguageExecutorImpl implements ScriptExpressionLanguageExecutor {
	/**
	 * L'engine d'exécution des script.
	 */
	private final ScriptEngine engine;

	/**

