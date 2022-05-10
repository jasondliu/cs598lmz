import io.netty.channel.ChannelHandlerContext;
import io.netty.channel.ChannelInboundHandlerAdapter;
import io.netty.handler.timeout.IdleState;
import io.netty.handler.timeout.IdleStateEvent;
import io.netty.util.ReferenceCountUtil;

import java.util.Date;

/**
 * Created by Administrator on 2017/7/26.
 */
public class HeartBeatServerHandler extends ChannelInboundHandlerAdapter {

    @Override
    public void channelRead(ChannelHandlerContext ctx, Object msg) throws Exception {
        System.out.println(new Date() + ": 服务端读到数据 -> " + msg);
        if (msg instanceof CustomProtocol) {
            CustomProtocol customProtocol = (CustomProtocol) msg;
            System.out.println(new Date() + ": 收到客户端的心跳 -> " + customProtocol.getContent());
        }
        ReferenceCountUtil.release(msg);
    }

   
