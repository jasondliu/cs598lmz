import io.netty.channel.ChannelHandlerContext;
import io.netty.channel.ChannelInboundHandlerAdapter;
import io.netty.handler.timeout.IdleState;
import io.netty.handler.timeout.IdleStateEvent;
import io.netty.util.ReferenceCountUtil;

import java.util.Date;

/**
 * @author yangtao__anxpp.com
 * @version 1.0
 */
public class HeartBeatServerHandler extends ChannelInboundHandlerAdapter {
    @Override
    public void channelRead(ChannelHandlerContext ctx, Object msg) throws Exception {
        try {
            if (msg instanceof String) {
                String message = (String) msg;
                System.out.println(new Date() + ": 客户端消息: " + message);
                if ("Heartbeat".equals(message)) {
                    ctx.write("has read message from client");
                    ctx.flush();
                }
            }
        } finally {
            ReferenceCountUtil.release(msg);
       
