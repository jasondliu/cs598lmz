import io.netty.buffer.ByteBuf;
import io.netty.channel.ChannelFutureListener;
import io.netty.channel.ChannelHandlerContext;
import io.netty.handler.codec.ByteToMessageDecoder;
import io.netty.util.AttributeKey;
import org.tachyonlog.model.Entry;
import org.tachyonlog.model.Entries;
import org.tachyonlog.util.EntryDecoder;

import java.nio.charset.Charset;
import java.util.List;

/**
 * Created by paul on 5/3/14.
 */
public class LogDecoder extends ByteToMessageDecoder {
    private AttributeKey<Entries> entriesAttributeKey;
    private Charset charset;

    public LogDecoder(final AttributeKey<Entries> entriesAttributeKey, final Charset charset) {
        this.entriesAttributeKey = entriesAttributeKey;
        this.charset = charset;
    }

    @Override
    protected void decode(final ChannelHandlerContext context
