import io.netty.handler.codec.MessageToMessageDecoder;

/**
 * Created by Administrator on 2019/3/27.
 */
public class MyLongToByteEncoder extends MessageToByteEncoder<Long> {
    @Override
    protected void encode(ChannelHandlerContext ctx, Long msg, ByteBuf out) throws Exception {
        System.out.println("MyLongToByteEncoder encode被调用");
        System.out.println("msg="+msg);
        out.writeLong(msg);
    }
}
