import io.netty.channel.ChannelHandlerContext;
import io.netty.channel.ChannelInboundHandlerAdapter;
import io.netty.util.concurrent.Future;
import io.netty.util.concurrent.GenericFutureListener;

public class NettyClientHandler extends ChannelInboundHandlerAdapter {
	
	private static final Logger logger = LoggerFactory.getLogger(NettyClientHandler.class);
	
	private static final int MAX_RETRY = 5;
	private int currentRetry = 0;
	private NettyClient client;
	private ChannelHandlerContext ctx;
	
	public NettyClientHandler(NettyClient client) {
		this.client = client;
	}
	
	@Override
	public void channelActive(ChannelHandlerContext ctx) throws Exception {
		this.ctx = ctx;
		logger.info("connect to server success");
	}
	
	@Override
	public void channelInactive(ChannelHandlerContext ctx) throws Exception {
		logger.info("connect to server lost");
		if (
