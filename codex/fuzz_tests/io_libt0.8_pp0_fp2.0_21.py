import io.netty.buffer.Unpooled;
import io.netty.channel.ChannelFutureListener;
import io.netty.channel.ChannelHandler;
import io.netty.channel.ChannelHandlerContext;
import io.netty.channel.ChannelInboundHandlerAdapter;
import io.netty.util.CharsetUtil;

import java.util.concurrent.atomic.AtomicInteger;

/**
 * @author qinjp
 * @date 2020-05-12
 **/
@ChannelHandler.Sharable
public class DiscardServerHandler extends ChannelInboundHandlerAdapter {
    private AtomicInteger count = new AtomicInteger(1);

    @Override
    public void channelRead(ChannelHandlerContext ctx, Object msg) throws Exception {
        count.incrementAndGet();
        ByteBuf in = (ByteBuf) msg;
        try {
            System.out.println(count + ":" + Thread.currentThread().getName() + "client:" + in.toString(CharsetUtil.UTF_8));
        } finally {
            in.release();
        }
