import io.tekniq.config.MapTqConfigProvider;
import io.tekniq.listener.TqExceptionListener;
import io.tekniq.listener.TqReadListener;
import io.tekniq.listener.TqWriteListener;
import io.tekniq.jdbc.TqJdbcConnectionProvider;
import org.junit.BeforeClass;
import org.junit.Test;

import java.sql.Connection;
import java.sql.Statement;
import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;

public class H2TqDataSourceTests {
    @BeforeClass
    public static void setupClass() throws Exception {
        TqConfig config = new TqConfig();
        TqConfigProvid
