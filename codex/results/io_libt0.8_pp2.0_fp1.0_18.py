import io.netty.handler.codec.http.HttpResponseStatus;

import java.net.InetSocketAddress;
import java.util.Map;

/**
 * @author luoming
 * @since 2020/7/15
 */
public class HttpRequestHandler extends SimpleChannelInboundHandler<FullHttpRequest> {

    private Map<String, Object> handlerMap;

    public HttpRequestHandler(Map<String, Object> handlerMap) {
        this.handlerMap = handlerMap;
    }

    @Override
    protected void channelRead0(ChannelHandlerContext ctx, FullHttpRequest request) throws Exception {
        if (!request.decoderResult().isSuccess()) {
            sendError(ctx, HttpResponseStatus.BAD_REQUEST);
            return;
        }
        if (request.method() != HttpMethod.GET) {
            sendError(ctx, HttpResponseStatus.METHOD_NOT_ALLOWED);
            return;
        }
        final String uri = request.uri();
        final String path = sanitizeUri(uri);
        if (
