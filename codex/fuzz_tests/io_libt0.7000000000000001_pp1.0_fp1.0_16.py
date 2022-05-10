import io.netty.channel.socket.SocketChannel;
import io.netty.util.concurrent.Future;
import io.netty.util.concurrent.GenericFutureListener;
import io.netty.util.concurrent.Promise;

import java.net.SocketAddress;
import java.util.concurrent.TimeUnit;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import com.github.taojintianxia.consensus.ratis.databasereplicated.client.network.handler.RaftClientHandler;

/**
 * @author Nianjun Sun
 * @date 2020/5/19 11:44
 */
public class RaftClientBootstrap {

    private static final Logger LOG = LoggerFactory.getLogger(RaftClientBootstrap.class);

    private EventLoopGroup workerGroup;
    private Bootstrap bootstrap;
    private ChannelFuture channelFuture;

    public RaftClientBootstrap() {
        // Configure the client.
        workerGroup = new NioEventLoopGroup
