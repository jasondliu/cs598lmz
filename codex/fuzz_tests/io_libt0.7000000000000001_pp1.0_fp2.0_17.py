import io.siddhi.core.event.Event;
import io.siddhi.extension.store.rdbms.util.RDBMSTableTestUtils;
import org.apache.commons.logging.Log;
import org.apache.commons.logging.LogFactory;
import org.testng.Assert;
import org.testng.annotations.AfterClass;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.Test;

import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.atomic.AtomicInteger;

public class UpdateOrInsertRDBMSTableTestCaseIT {
    private static final Log log = LogFactory.getLog(UpdateOrInsertRDBMSTableTestCaseIT.class);
    private List<InMemoryRDBMSTable> rdbmsTables = new ArrayList<>();
    private static final String TABLE_NAME = "T
