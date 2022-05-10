import io.netty.channel.ChannelHandlerContext;
import io.netty.channel.ChannelInboundHandlerAdapter;
import io.netty.channel.socket.SocketChannel;

public class AcceptorHandler extends ChannelInboundHandlerAdapter{
	
	private Logger logger = Logger.getLogger(AcceptorHandler.class);
	
	@Override
	public void channelActive(ChannelHandlerContext ctx) throws Exception {
		logger.info("新客户端连接进来了："+ctx.channel().remoteAddress());
		//把当前channel加入到channelGroup中
		SocketChannelManager.channelGroup.add(ctx.channel());
	}
	
	@Override
	public void channelInactive(ChannelHandlerContext ctx) throws Exception {
		logger.info("客户端关闭了连接："+ctx.channel().remoteAddress());
		//把当前channel从channelGroup中
