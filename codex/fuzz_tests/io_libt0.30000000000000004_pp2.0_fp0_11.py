import io.netty.channel.ChannelHandlerContext;
import io.netty.channel.ChannelInboundHandlerAdapter;
import io.netty.handler.timeout.IdleState;
import io.netty.handler.timeout.IdleStateEvent;
import io.netty.util.ReferenceCountUtil;
import org.apache.log4j.Logger;

import java.io.IOException;

/**
 * Created by Administrator on 2016/9/27.
 */
public class HeartBeatClientHandler extends ChannelInboundHandlerAdapter {
    private static final Logger logger = Logger.getLogger(HeartBeatClientHandler.class);

    @Override
    public void channelRead(ChannelHandlerContext ctx, Object msg) throws Exception {
        try {
            if (msg instanceof String) {
                logger.info("HeartBeatClientHandler channelRead :" + msg);
            } else {
                logger.info("HeartBeatClientHandler channelRead :" + msg);
            }
        } finally {
            ReferenceCountUtil.release(msg);
        }
    }

    @Override
    public
