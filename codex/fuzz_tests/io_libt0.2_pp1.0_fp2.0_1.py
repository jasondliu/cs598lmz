import io.netty.channel.ChannelHandlerContext;
import io.netty.channel.ChannelInboundHandlerAdapter;
import io.netty.handler.timeout.IdleState;
import io.netty.handler.timeout.IdleStateEvent;
import io.netty.util.ReferenceCountUtil;

import java.util.Date;

/**
 * Created by Administrator on 2017/4/19.
 */
public class HeartBeatServerHandler extends ChannelInboundHandlerAdapter {

    @Override
    public void channelRead(ChannelHandlerContext ctx, Object msg) throws Exception {
        try {
            NettyMessage message = (NettyMessage) msg;
            // 握手成功，主动发送心跳消息
            if (message.getHeader() != null
                    && message.getHeader().getType() == MessageType.LOGIN_RESP.value()) {
                ctx.writeAndFlush(buildHeatBeat());
            } else if (message.getHeader() != null
                    && message.getHeader().
