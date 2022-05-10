import io.netty.channel.ChannelOption;
import io.netty.channel.EventLoopGroup;
import io.netty.channel.nio.NioEventLoopGroup;
import io.netty.channel.socket.nio.NioSocketChannel;
import io.netty.handler.codec.http.HttpClientCodec;

import java.net.InetSocketAddress;
import java.util.List;
import java.util.concurrent.BlockingQueue;

import com.barchart.netty.api.NettyChannel;
import com.barchart.netty.api.NettyRouter;
import com.barchart.netty.api.NettyService;
import com.barchart.netty.common.messages.ResponseMessage;

/**
 * Create and start a Netty server.
 */
public class NettyClient implements NettyService {

	private final BlockingQueue<ResponseMessage> queue;
	private final InetSocketAddress remote;
	private final NettyRouter router;

	private volatile Channel channel;
	private volatile boolean closed
