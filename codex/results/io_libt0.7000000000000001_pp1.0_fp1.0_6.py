import io.netty.channel.ChannelOption;
import io.netty.channel.EventLoopGroup;
import io.netty.channel.nio.NioEventLoopGroup;
import io.netty.channel.socket.SocketChannel;
import io.netty.channel.socket.nio.NioSocketChannel;
import io.netty.handler.codec.string.StringDecoder;
import io.netty.handler.codec.string.StringEncoder;
import io.netty.handler.logging.LogLevel;
import io.netty.handler.logging.LoggingHandler;

public class NettyClient {

	private static final StringDecoder DECODER = new StringDecoder();
	private static final StringEncoder ENCODER = new StringEncoder();

	private static final ChannelOption<Integer> CONNECT_TIMEOUT = ChannelOption.valueOf("connectTimeoutMillis");

	private static final StringBootstrapFactory BOOTSTRAP_FACTORY = new StringBootstrapFactory();

	private static final EventLoopGroup EVENT_LOOP_GROUP = new NioEventLoopGroup
