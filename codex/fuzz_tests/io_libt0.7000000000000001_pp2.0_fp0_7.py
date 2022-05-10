import io.netty.util.concurrent.DefaultThreadFactory;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.net.InetAddress;
import java.net.InetSocketAddress;
import java.net.UnknownHostException;
import java.util.HashMap;
import java.util.Map;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;

public class NettyRemotingClient implements RemotingClient {
    private static final Logger LOG = LoggerFactory.getLogger(NettyRemotingClient.class);

    private static final long LOCK_TIMEOUT = 3000;

    private Bootstrap bootstrap = null;

    private EventLoopGroup workerGroup = null;

    private static final int workerThreadNum = 8;

    private static final ExecutorService publicExecutor = Executors.newFixedThreadPool(workerThreadNum, new DefaultThreadFactory("NettyClientPublicExecutor"));

    private final Netty
