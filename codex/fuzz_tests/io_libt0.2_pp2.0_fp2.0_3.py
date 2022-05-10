import io.netty.channel.ChannelHandlerContext;
import io.netty.channel.SimpleChannelInboundHandler;
import io.netty.handler.codec.http.FullHttpRequest;
import io.netty.handler.codec.http.HttpResponseStatus;
import io.netty.util.CharsetUtil;

import java.util.HashMap;
import java.util.Map;

/**
 * Created by zhangyunfei on 16/9/21.
 */
public class HttpServerHandler extends SimpleChannelInboundHandler<FullHttpRequest> {

    @Override
    protected void channelRead0(ChannelHandlerContext ctx, FullHttpRequest msg) throws Exception {
        if (msg.getMethod().name().equals("GET")) {
            Map<String, Object> map = new HashMap<>();
            map.put("name", "zhangyunfei");
            map.put("age", "18");
            String json = JsonUtil.toJson(map);
            FullHttpResponse response = new DefaultFullHttpResponse(HttpVersion.HTTP_
