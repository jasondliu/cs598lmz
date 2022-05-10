import io.netty.channel.ChannelHandlerContext;
import io.netty.channel.ChannelInboundHandlerAdapter;
import io.netty.util.ReferenceCountUtil;

/**
 * @author zhouliang
 * @since 2018-06-19 14:06
 **/
public class ServerHandler extends ChannelInboundHandlerAdapter {

    @Override
    public void channelRead(ChannelHandlerContext ctx, Object msg) throws Exception {
        try {
            ByteBuf buf = (ByteBuf) msg;
            byte[] req = new byte[buf.readableBytes()];
            buf.readBytes(req);
            String body = new String(req, "UTF-8");
            System.out.println("Server :" + body );
            String response = "进行返回给客户端的响应：" + body ;
            ctx.writeAndFlush(Unpooled.copiedBuffer(response.getBytes()));
        } finally {
            ReferenceCountUtil.release(msg);
        }
    }

   
