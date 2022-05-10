import io.netty.channel.ChannelHandlerContext;
import io.netty.channel.ChannelInboundHandlerAdapter;
import io.netty.handler.timeout.IdleState;
import io.netty.handler.timeout.IdleStateEvent;
import io.netty.util.ReferenceCountUtil;

public class NettyClientHandler extends ChannelInboundHandlerAdapter {
	private static final Logger logger = LoggerFactory.getLogger(NettyClientHandler.class);
	private NettyClient client;
	private String clientId;

	public NettyClientHandler(NettyClient client, String clientId) {
		this.client = client;
		this.clientId = clientId;
	}

	@Override
	public void channelActive(ChannelHandlerContext ctx) throws Exception {
		logger.info("NettyClientHandler channelActive");
		client.setConnectStatus(true);
		client.setCtx(ctx);
		client.heartBeat();
	}

	@Override
	public void channelInactive(ChannelHandlerContext ctx) throws Exception {

