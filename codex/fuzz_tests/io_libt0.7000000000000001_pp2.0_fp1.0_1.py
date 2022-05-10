import io.netty.handler.codec.http.websocketx.TextWebSocketFrame;
import org.apache.logging.log4j.Logger;
import org.apache.logging.log4j.LogManager;

/**
 * Created by Anton on 27.01.2017.
 */
public class WebSocketServerHandler extends SimpleChannelInboundHandler<TextWebSocketFrame> {
    private static final Logger log = LogManager.getLogger(WebSocketServerHandler.class);

    @Override
    public void channelRead0(ChannelHandlerContext ctx, TextWebSocketFrame msg) throws Exception {
        log.info("channelRead0");
        // Send the uppercase string back.
        String request = msg.text();
        log.info(request);
        ctx.channel().writeAndFlush(new TextWebSocketFrame(request.toUpperCase()));
    }

    @Override
    public void exceptionCaught(ChannelHandlerContext ctx, Throwable cause) {
        log.info("exceptionCaught");
        cause.printStackTrace();
        ctx.
