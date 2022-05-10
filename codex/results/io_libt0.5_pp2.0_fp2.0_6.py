import io.netty.handler.codec.http.websocketx.WebSocketFrame;

/**
 * @author liuya
 * @date 2018/7/27
 */
public class WebSocketFrameHandler extends SimpleChannelInboundHandler<WebSocketFrame> {

    @Override
    protected void channelRead0(ChannelHandlerContext ctx, WebSocketFrame msg) throws Exception {
        // handle WebSocket frame
    }
}
