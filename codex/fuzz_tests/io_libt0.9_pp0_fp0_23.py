import io.netty.util.CharsetUtil;

/**
 * @author Evan
 * @since 2020.3.29
 */
public class MySeverHandler extends SimpleChannelInboundHandler<ByteBuf> {
    @Override
    protected void channelRead0(ChannelHandlerContext ctx, ByteBuf msg) throws Exception {
        final ByteBuf buffer = ctx.alloc().buffer();
        buffer.writeBytes("Received".getBytes(CharsetUtil.UTF_8));
        ctx.writeAndFlush(buffer);
    }
}
