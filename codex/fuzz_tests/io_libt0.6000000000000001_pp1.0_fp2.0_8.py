import io.netty.channel.ChannelHandlerContext;
import io.netty.handler.timeout.IdleState;
import io.netty.handler.timeout.IdleStateEvent;

/**
 * @author : yangxh
 * @version : 1.0
 * @create 2018-10-11 15:00
 * @Team :
 **/
public class HeartbeatHandler extends ChannelInboundHandlerAdapter {

    @Override
    public void userEventTriggered(ChannelHandlerContext ctx, Object evt) throws Exception {
        if (evt instanceof IdleStateEvent) {
            IdleStateEvent event = (IdleStateEvent) evt;
            if (event.state() == IdleState.READER_IDLE) {
                System.out.println("长期没收到客户端的信息了，关闭通道");
                ctx.close();
            } else if (event.state() == IdleState.WRITER_IDLE) {
                System.out.println("
