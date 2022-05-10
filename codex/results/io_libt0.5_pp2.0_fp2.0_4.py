import io.netty.channel.ChannelHandlerContext;
import io.netty.channel.ChannelInboundHandlerAdapter;
import io.netty.channel.SimpleChannelInboundHandler;
import io.netty.handler.timeout.IdleStateEvent;
import io.netty.util.ReferenceCountUtil;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.util.concurrent.TimeUnit;

/**
 * Created by zhangyun on 5/16/18.
 */
public class HeartbeatServerHandler extends SimpleChannelInboundHandler<RequestInfo> {

    private static final Logger LOGGER = LoggerFactory.getLogger(HeartbeatServerHandler.class);

    @Override
    protected void channelRead0(ChannelHandlerContext ctx, RequestInfo msg) throws Exception {
        if(msg instanceof HeartbeatInfo) {
            HeartbeatInfo heartbeatInfo = (HeartbeatInfo) msg;
            LOGGER.info("heartbeatInfo: " + heartbeatInfo.toString());
        } else {
            LOGGER.info("request
