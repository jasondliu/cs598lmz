import io.netty.channel.ChannelHandlerContext;
import io.netty.handler.codec.http.websocketx.TextWebSocketFrame;
import io.netty.handler.codec.http.websocketx.WebSocketFrame;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

/**
 * @author zhongjun - zj@akka.com
 * @since 1.0.0
 */
public class WebSocketFrameHandler extends AbstractFrameHandler {

    private static final Logger LOGGER = LoggerFactory.getLogger(WebSocketFrameHandler.class);

    public WebSocketFrameHandler(ChannelHandlerContext ctx) {
        super(ctx);
    }

    @Override
    public void channelRead(ChannelHandlerContext ctx, Object msg) throws Exception {
        WebSocketFrame frame = (WebSocketFrame) msg;
        if (frame instanceof TextWebSocketFrame) {
            String text = ((TextWebSocketFrame) frame).text();
            //TODO Handle Message
            LOGGER.info("Text Message
