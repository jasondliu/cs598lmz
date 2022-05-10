import io.netty.buffer.ByteBuf;
import io.netty.channel.ChannelFuture;
import io.netty.channel.ChannelHandler.Sharable;
import io.netty.channel.ChannelHandlerContext;
import io.netty.channel.ChannelInboundHandlerAdapter;

/**
 * Created by Tan on 2016/3/24 0024.
 */
public class PacketSenderHandler extends ChannelInboundHandlerAdapter {

    @Override
    public void channelActive(ChannelHandlerContext ctx) throws Exception {
        String content = "Hello World!\r\n";
        byte[] contentBytes = content.getBytes("utf-8");
        Packet packet = new Packet((short) 1, new byte[0], contentBytes);

        ByteBuf buf = ctx.alloc().buffer();
        packet.toByteBuf(buf);

        ChannelFuture future = ctx.writeAndFlush(buf);
        future.addListener(new ChannelFutureListener() {
            @Override
            public void operationComplete(ChannelFuture future) throws Exception {
                if (future.isSuccess()) {
                   
