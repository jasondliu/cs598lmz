import io.netty.buffer.ByteBuf;
import io.netty.channel.ChannelHandlerContext;
import io.netty.handler.codec.MessageToByteEncoder;

import java.nio.charset.Charset;

public class MsgEncoder extends MessageToByteEncoder<Msg> {

  @Override
  protected void encode(ChannelHandlerContext ctx, Msg msg, ByteBuf out) throws Exception {
    if (msg == null || msg.getHeader() == null) {
      throw new Exception("the encode message is null");
    }
    Header header = msg.getHeader();
    // 先将消息长度写入，也就是消息头的dataLength
    out.writeInt(header.getDataLength());
    out.writeInt(header.getDataLength());
    out.writeInt(header.getDataLength());
    out.writeInt(header.getDataLength());
    out.writeInt(header.getDataLength());
    out.
