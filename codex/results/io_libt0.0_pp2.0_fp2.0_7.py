import io.netty.channel.ChannelHandlerContext;
import io.netty.channel.ChannelInboundHandlerAdapter;
import io.netty.handler.timeout.IdleState;
import io.netty.handler.timeout.IdleStateEvent;
import io.netty.util.ReferenceCountUtil;

import java.util.Date;

/**
 * @author zhangbo
 */
public class HeartbeatServerHandler extends ChannelInboundHandlerAdapter {

    @Override
    public void channelRead(ChannelHandlerContext ctx, Object msg) throws Exception {
        try {
            if (msg instanceof RequestInfo) {
                RequestInfo requestInfo = (RequestInfo) msg;
                System.out.println("服务端接收到客户端的心跳信息：" + requestInfo.toString());
            } else {
                System.out.println("服务端接收到客户端的消息：" + msg);
           
