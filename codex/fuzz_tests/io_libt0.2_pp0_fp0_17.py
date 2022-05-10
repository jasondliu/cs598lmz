import io.netty.channel.ChannelHandlerContext;
import io.netty.channel.ChannelInboundHandlerAdapter;
import io.netty.handler.timeout.IdleState;
import io.netty.handler.timeout.IdleStateEvent;
import io.netty.util.ReferenceCountUtil;

import java.util.concurrent.atomic.AtomicInteger;

/**
 * @author zhangxinpeng
 * @date 2019-08-29
 */
public class HeartbeatServerHandler extends ChannelInboundHandlerAdapter {
    private static final AtomicInteger counter = new AtomicInteger(0);

    @Override
    public void channelRead(ChannelHandlerContext ctx, Object msg) throws Exception {
        try {
            String message = (String) msg;
            System.out.println("server receive message: " + message);
            String response = "I am ok";
            ctx.writeAndFlush(Unpooled.copiedBuffer(response.getBytes()));
        } finally {
            ReferenceCountUtil.release(msg);
        }
    }

    @Override
    public
