import io.github.osvaldjr.core.objects.enums.Mode;
import io.github.osvaldjr.core.objects.events.ExtentEvents;
import io.github.osvaldjr.core.objects.events.testinfo.TestInfo;
import io.github.osvaldjr.core.objects.exceptions.CucumberReportException;
import io.github.osvaldjr.core.objects.filters.CucumberReportFilter;
import io.github.osvaldjr.core.objects.models.CucumberFeature;
import io.github.osvaldjr.core.objects.models.ReportsCucumberModel;
import io.github.osvaldjr.core.utils.Utils;
import lombok.Getter;
import lombok.Setter;

public class ReportsGlobals {

  private static final String RED_COLOR = "red";
  private static final String GREEN_COLOR = "green";

  @Getter private static ReportsCucumberModel reportsModel = new ReportsCucumberModel();
