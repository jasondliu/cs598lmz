import io.github.nixtabyte.telegram.jtelebot.response.json.Message;
import io.github.nixtabyte.telegram.jtelebot.server.Command;
import io.github.nixtabyte.telegram.jtelebot.server.CommandFactory;
import org.apache.commons.configuration.PropertiesConfiguration;
import org.apache.commons.lang.StringUtils;
import org.apache.log4j.Logger;

import java.net.InetAddress;
import java.net.UnknownHostException;

/**
 * Created by jonathan on 19/08/16.
 */
public class DefaultCommandFactory implements CommandFactory {

    private static final Logger LOG = Logger.getLogger(DefaultCommandFactory.class);

    private static final String COMMAND_HELP = "help";
    private static final String COMMAND_START = "start";
    private static final String COMMAND_STOP = "stop";
    private static final String COMMAND_STATUS = "status";
    private static final String COMMAND_LOCATION = "location";
