import io.netty.channel.ChannelHandlerContext;
import io.netty.channel.ChannelInboundHandlerAdapter;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;

public class ChannelHandlerIdleStateHandlerTest {

    private static final long readerIdleTimeMillis = 1000;
    private static final long writerIdleTimeMillis = 300;
    private static final long allIdleTimeMillis = 300;

    private static final ChannelHandlerIdleStateHandler lastIdleStateHandler =
            new ChannelHandlerIdleStateHandler(readerIdleTimeMillis, writerIdleTimeMillis, allIdleTimeMillis);

    private static final ChannelHandlerIdleStateHandler firstIdleStateHandler =
            new ChannelHandlerIdleStateHandler(readerIdleTimeMillis, writerIdleTimeMillis, allIdleTimeMillis);

    @Test
    public void testReaderIdle() throws Exception {
        EmbeddedChannel ch = new EmbeddedChannel(lastIdleStateHandler
