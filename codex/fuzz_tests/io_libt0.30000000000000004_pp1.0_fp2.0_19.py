import io.netty.channel.ChannelHandlerContext;
import io.netty.channel.ChannelInboundHandlerAdapter;
import io.netty.util.ReferenceCountUtil;

import java.util.concurrent.atomic.AtomicInteger;

/**
 * @author zhangjianbin
 *
 */
public class ClientHandler extends ChannelInboundHandlerAdapter {

	private AtomicInteger counter = new AtomicInteger(0);

	@Override
	public void channelRead(ChannelHandlerContext ctx, Object msg)
			throws Exception {
		try {
			String body = (String) msg;
			System.out.println("Now is : " + body + " ; the counter is : "
					+ counter.incrementAndGet());
		} finally {
			ReferenceCountUtil.release(msg);
		}
	}

	@Override
	public void exceptionCaught(ChannelHandlerContext ctx, Throwable cause)
			throws Exception {
		cause.printStackTrace();
		ctx.close();
	}
