import io.netty.channel.ChannelHandlerContext;
import io.netty.handler.codec.MessageToByteEncoder;

public class MessageEncoder extends MessageToByteEncoder<Message> {

	@Override
	protected void encode(ChannelHandlerContext ctx, Message msg, ByteBuf out) throws Exception {
		out.writeShort(msg.getLength());
		out.writeShort(msg.getCmd());
		out.writeShort(msg.getSeq());
		out.writeBytes(msg.getBody());
	}

}
