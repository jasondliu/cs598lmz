import io.netty.buffer.ByteBuf;
import io.netty.channel.ChannelHandlerContext;
import io.netty.handler.codec.ByteToMessageCodec;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

import java.util.List;

public class Codec extends ByteToMessageCodec<Message<?>> {
    private static final Logger logger = LogManager.getLogger(Codec.class);

    @Override
    protected void encode(ChannelHandlerContext ctx, Message<?> msg, ByteBuf buf) throws Exception {
        logger.debug("Sending: {} {}", msg.type(), msg);
        buf.writeInt(msg.type().ordinal());
        msg.encode(buf);
    }

    @Override
    protected void decode(ChannelHandlerContext ctx, ByteBuf buf, List<Object> out) throws Exception {
        if (buf.readableBytes() < 4) {
            return;
        }
        buf.markReaderIndex();
        int type =
