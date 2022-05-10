import io.netty.buffer.Unpooled;
import io.netty.util.CharsetUtil;

public class ClientHandler extends ChannelInboundHandlerAdapter {

    @Override
    public void channelActive(ChannelHandlerContext ctx) throws Exception {
//        ctx.writeAndFlush(Unpooled.copiedBuffer("helloServer", CharsetUtil.UTF_8));
        System.out.println("send data ...");
        ctx.flush();
    }

    @Override
    public void channelRead(ChannelHandlerContext ctx, Object msg) throws Exception {
        System.out.println("client channel read ...");
        ByteBuf buf = (ByteBuf) msg;
        System.out.println("收到服务器数据：" + buf.toString(CharsetUtil.UTF_8));
    }

    @Override
    public void channelUnregistered(ChannelHandlerContext ctx) throws Exception {
        System.out.println("client channel unregistered ...");
    }

    @Override
    public
