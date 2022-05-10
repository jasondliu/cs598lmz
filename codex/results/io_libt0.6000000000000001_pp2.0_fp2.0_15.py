import io.github.prolobjectlink.db.ObjectConverter;
import io.github.prolobjectlink.db.etc.Settings;
import io.github.prolobjectlink.db.prolog.PrologDatabaseEngine;
import io.github.prolobjectlink.db.prolog.PrologDatabaseProvider;
import io.github.prolobjectlink.logging.LoggerConstants;
import io.github.prolobjectlink.logging.LoggerUtils;

/** @author Jose Zalacain @since 1.0 */
public final class PrologObjectConverter extends AbstractConverter implements ObjectConverter {

	private final PrologDatabaseProvider provider;
	private final PrologDatabaseEngine engine;

	public PrologObjectConverter(PrologDatabaseProvider provider, PrologDatabaseEngine engine) {
		this.provider = provider;
		this.engine = engine;
	}

	public String toString(Object object) {

		if (object == null) {
			return "null";
		}

		if (object instanceof
