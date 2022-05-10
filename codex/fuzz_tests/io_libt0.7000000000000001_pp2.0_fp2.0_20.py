import io.github.mzmine.datamodel.RawDataFile;
import io.github.mzmine.datamodel.Scan;
import io.github.mzmine.main.MZmineCore;
import io.github.mzmine.modules.MZmineModuleCategory;
import io.github.mzmine.modules.MZmineProcessingModule;
import io.github.mzmine.parameters.ParameterSet;
import io.github.mzmine.taskcontrol.Task;
import io.github.mzmine.util.ExitCode;

public class PeakPickerModule implements MZmineProcessingModule {

	private static final Logger logger = LoggerFactory.getLogger(PeakPicker.class);

	private static final String MODULE_NAME = "Peak picking";
	private static final String MODULE_DESCRIPTION = "Peak picking.";

	@Override
	public @Nonnull String getName() {
		return MODULE_NAME;
	}

	@Override
	public @Nonnull String getDescription() {
		return MODULE_DESCRIPTION;
