import io.netty.channel.Channel;
import io.netty.channel.ChannelHandler;
import io.netty.channel.ChannelHandlerContext;
import io.netty.channel.ChannelInboundHandlerAdapter;
import io.netty.util.concurrent.EventExecutorGroup;

import java.util.concurrent.TimeUnit;

public class ServerHeartBeatHandler extends ChannelInboundHandlerAdapter {

    //客户端超时时间
    private static final int READ_WAIT_SECONDS=15;

    @Override
    public void channelRead(ChannelHandlerContext ctx, Object msg) throws Exception {
        //在服务端每次有数据读取的时候, 就将读超时时间 刷新
        if(msg instanceof MessageProtocol){
            MessageProtocol messageProtocol = (MessageProtocol) msg;
            System.out.println("Server 收到消息:"+new String
