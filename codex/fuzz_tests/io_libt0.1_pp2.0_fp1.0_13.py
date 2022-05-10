import io.netty.channel.ChannelHandlerContext;
import io.netty.channel.ChannelInboundHandlerAdapter;
import io.netty.handler.timeout.IdleState;
import io.netty.handler.timeout.IdleStateEvent;
import io.netty.util.ReferenceCountUtil;

/**
 * @author: zhangc/jaguar_zc@sina.com
 * @create: 2020-08-20 09:49
 */
public class HeartBeatClientHandler extends ChannelInboundHandlerAdapter {

    private static final Logger logger = LoggerFactory.getLogger(HeartBeatClientHandler.class);

    @Override
    public void channelRead(ChannelHandlerContext ctx, Object msg) throws Exception {
        try {
            if (msg instanceof String) {
                String message = (String) msg;
                logger.info("Client receive message: {}", message);
            } else {
                logger.error("Client receive message type is not String!");
            }
        } finally {
            ReferenceCountUtil.release(msg);
        }
    }

    @
