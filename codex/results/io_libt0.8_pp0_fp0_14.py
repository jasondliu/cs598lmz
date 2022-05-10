import io.netty.buffer.ByteBuf;
import io.netty.channel.ChannelHandlerContext;
import io.netty.handler.codec.MessageToByteEncoder;

/**
 * @author iceWang
 * @date 2020/1/19
 * @description 集成 Netty 的序列化框架 MessageToByteEncoder
 */
public class TankMsgEncoder extends MessageToByteEncoder<TankMsg> {
    @Override
    protected void encode(ChannelHandlerContext ctx, TankMsg msg, ByteBuf byteBuf) throws Exception {
        byteBuf.writeInt(msg.x);
        byteBuf.writeInt(msg.y);
    }
}
