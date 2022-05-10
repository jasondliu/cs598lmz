import io.netty.channel.ChannelHandlerContext;
import io.netty.channel.ChannelInboundHandlerAdapter;
import io.netty.handler.timeout.IdleState;
import io.netty.handler.timeout.IdleStateEvent;

/**
 * Created by Administrator on 2017/8/7.
 */
public class HeartBeatServerHandler extends ChannelInboundHandlerAdapter {

    @Override
    public void userEventTriggered(ChannelHandlerContext ctx, Object evt) throws Exception {
        if (evt instanceof IdleStateEvent) {
            IdleStateEvent event = (IdleStateEvent) evt;
            if (event.state() == IdleState.READER_IDLE) {
                System.out.println("READER_IDLE");
            } else if (event.state() == IdleState.WRITER_IDLE) {
                System.out.println("WRITER_IDLE");
            } else if (event.state() == IdleState.ALL_IDLE) {
                System.out.println("ALL_IDLE");
            }
        }
    }
