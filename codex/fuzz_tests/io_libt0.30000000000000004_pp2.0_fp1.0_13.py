import io.netty.channel.ChannelHandlerContext;
import io.netty.channel.ChannelInboundHandlerAdapter;
import io.netty.handler.timeout.IdleState;
import io.netty.handler.timeout.IdleStateEvent;
import org.apache.log4j.Logger;

import java.util.concurrent.atomic.AtomicInteger;

/**
 * Created by wangyong on 2017/7/6.
 */
public class HeartBeatServerHandler extends ChannelInboundHandlerAdapter {

    private static final Logger logger = Logger.getLogger(HeartBeatServerHandler.class);

    private static final AtomicInteger atomicInteger = new AtomicInteger(0);

    @Override
    public void userEventTriggered(ChannelHandlerContext ctx, Object evt) throws Exception {
        if (evt instanceof IdleStateEvent) {
            IdleStateEvent event = (IdleStateEvent) evt;
            if (event.state() == IdleState.READER_IDLE) {
                logger.info("READER_IDLE");
                ctx.close();
            }
