import io.netty.handler.codec.http.HttpResponseStatus;
import io.netty.handler.codec.http.HttpVersion;
import io.netty.handler.codec.http.websocketx.WebSocketServerHandshaker;
import io.netty.handler.codec.http.websocketx.WebSocketServerHandshakerFactory;
import io.netty.util.AttributeKey;
import org.apache.commons.lang3.StringUtils;

import java.util.Objects;

/**
 * @author zhangxinpeng
 * @date 2019-05-15
 */
public class HttpRequestHandler extends SimpleChannelInboundHandler<FullHttpRequest> {
    private static final String WEBSOCKET_PATH = "/websocket";

    @Override
    protected void channelRead0(ChannelHandlerContext ctx, FullHttpRequest msg) throws Exception {
        String uri = msg.uri();
        if (StringUtils.equals(WEBSOCKET_PATH, uri)) {
            handWebsocket(ctx, msg);
       
