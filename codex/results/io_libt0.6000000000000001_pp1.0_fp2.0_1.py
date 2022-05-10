import io.netty.channel.ChannelHandlerContext;
import io.netty.handler.codec.MessageToMessageDecoder;
import java.util.List;

public class NettyKryoDecoder extends MessageToMessageDecoder<ByteBuf> {

  private final KryoSerialization kryoSerialization;

  public NettyKryoDecoder(KryoSerialization kryoSerialization) {
    this.kryoSerialization = kryoSerialization;
  }

  @Override
  protected void decode(ChannelHandlerContext ctx, ByteBuf msg, List<Object> out) throws Exception {
    int length = msg.readableBytes();
    byte[] array = new byte[length];
    msg.getBytes(msg.readerIndex(), array, 0, length);
    out.add(kryoSerialization.deserialize(array));
  }
}
