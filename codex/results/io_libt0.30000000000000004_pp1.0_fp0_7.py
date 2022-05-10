import io.netty.channel.ChannelHandlerContext;
import io.netty.channel.ChannelInboundHandlerAdapter;
import io.netty.handler.timeout.IdleState;
import io.netty.handler.timeout.IdleStateEvent;
import io.netty.util.ReferenceCountUtil;

import java.util.concurrent.ScheduledFuture;
import java.util.concurrent.TimeUnit;

/**
 * @author zhangyifei
 */
public class HeartBeatClientHandler extends ChannelInboundHandlerAdapter {

    private ScheduledFuture<?> heartBeat;

    private Client client;

    public HeartBeatClientHandler(Client client) {
        this.client = client;
    }

    @Override
    public void channelRead(ChannelHandlerContext ctx, Object msg) throws Exception {
        try {
            if (msg instanceof String) {
                String message = (String) msg;
                if (message.equals(NettyConstant.PING)) {
                    ctx.writeAndFlush(NettyConstant.PONG);
                    System.out.println
