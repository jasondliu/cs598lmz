import io.netty.channel.group.*;

import org.neo4j.causalclustering.discovery.*;
import org.neo4j.causalclustering.NettyPipelineBuilderFactory;
import org.neo4j.causalclustering.logging.MessageLogger;
import org.neo4j.causalclustering.protocol.*;
import org.neo4j.helpers.AdvertisedSocketAddress;
import org.neo4j.kernel.configuration.Config;
import org.neo4j.kernel.lifecycle.LifecycleAdapter;
import org.neo4j.logging.Log;

import static org.neo4j.causalclustering.protocol.NettyPipelineBuilderFactory.*;

public class Server extends LifecycleAdapter
{
    private final Log log;
    private final MessageLogger<AdvertisedSocketAddress> messageLogger;
    private final UpstreamMessageHandlerSelector messageHandler;
    private final Server.Monitor monitor;

    private final Config remoteConfig;
