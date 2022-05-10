import io.netty.channel.SimpleChannelInboundHandler;

/**
 * @author xiey
 * @date 2019/7/4 17:20
 * @description：
 */
public class MyChatClientHandler extends SimpleChannelInboundHandler<String> {
    @Override
    protected void channelRead0(ChannelHandlerContext ctx, String msg) throws Exception {
        System.out.println(msg);
    }
}
