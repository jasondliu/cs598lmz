import io.r2dbc.spi.Row;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.util.ArrayList;
import java.util.Map;
import java.util.Set;

/**
 * The type Configurator.
 *
 * @author Charlie Zhang
 */
public class Configurator {
    private static final Logger LOG = LoggerFactory.getLogger(Configurator.class);
    private static final Configurator instance = new Configurator();

    /**
     * Gets instance.
     *
     * @return the instance
     */
    public static Configurator getInstance() {
        return instance;
    }

    private Configurator() {
    }

    /**
     * Gets hosts.
     *
     * @return the hosts
     */
    public Map<String, Set<String>> getHosts() {
        Set<String> hosts = TcpNode.getInstance().getHosts();

        //if config hosts is empty or not set, just get all the hosts
