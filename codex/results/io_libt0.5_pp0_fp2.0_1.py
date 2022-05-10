import io.netty.channel.socket.SocketChannel;
import io.netty.handler.codec.http.HttpObjectAggregator;
import io.netty.handler.codec.http.HttpServerCodec;
import io.netty.handler.stream.ChunkedWriteHandler;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Component;

/**
 * Created by Administrator on 2017/12/20.
 */
@Component
public class HttpServerInitializer extends ChannelInitializer<SocketChannel> {
    private static final Logger logger = LoggerFactory.getLogger(HttpServerInitializer.class);

    @Value("${netty.websocket.maxFrameLength}")
    private int maxFrameLength;

    @Override
    protected void initChannel(SocketChannel ch) throws Exception {
        logger.info("HttpServerInitializer initChannel");
        ChannelPipeline pipeline = ch.pipeline();

