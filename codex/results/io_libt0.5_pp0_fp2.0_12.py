import io.netty.channel.ChannelHandlerContext;
import io.netty.channel.ChannelInboundHandlerAdapter;
import io.netty.util.ReferenceCountUtil;

public class ClientHandler extends ChannelInboundHandlerAdapter {

    @Override
    public void channelActive(ChannelHandlerContext ctx) throws Exception {
        System.out.println("ClientHandler Active");
    }

    @Override
    public void channelRead(ChannelHandlerContext ctx, Object msg) throws Exception {
        try {
            FileRegion fileRegion = (FileRegion) msg;
            System.out.println("ClientHandler Read");
            System.out.println("fileRegion.count() = " + fileRegion.count());
            System.out.println("fileRegion.position() = " + fileRegion.position());
            System.out.println("fileRegion.transferred() = " + fileRegion.transferred());
            System.out.println("fileRegion.transfered() = " + fileRegion.transfered());
        } finally {
            ReferenceCountUtil.release(msg);
        }
    }

    @Override
