import io.netty.channel.ChannelHandlerContext;
import io.netty.channel.SimpleChannelInboundHandler;
import io.netty.handler.timeout.IdleStateEvent;
import io.netty.util.ReferenceCountUtil;

public class NettyClientHandler extends SimpleChannelInboundHandler<Message> {

	private static final Logger logger = LoggerFactory.getLogger(NettyClientHandler.class);

	private final NettyClient client;

	public NettyClientHandler(NettyClient client) {
		this.client = client;
	}

	@Override
	public void channelActive(ChannelHandlerContext ctx) throws Exception {
		logger.info("客户端连接成功");
	}

	@Override
	public void channelInactive(ChannelHandlerContext ctx) throws Exception {
		logger.info("客户端连接断开");
		client.doConnect();
	}

	@Override
	public void channelRead0(ChannelHandlerContext ctx, Message msg
