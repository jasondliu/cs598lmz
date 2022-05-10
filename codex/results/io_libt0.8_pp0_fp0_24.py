import io.netty.channel.ChannelHandlerContext;
import io.netty.handler.codec.http.websocketx.TextWebSocketFrame;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;

@Sharable
public class WebSocketHandler extends ChannelHandlerAdapter {

    private final Map<ChannelHandlerContext, WebSocketClientHandler> channelHandlerContext2WebSocketClientHandlerMap;
    private final List<WebSocketClientHandler> webSocketClientHandlerList;

    public WebSocketHandler(Map<ChannelHandlerContext, WebSocketClientHandler> channelHandlerContext2WebSocketClientHandlerMap,
                            List<WebSocketClientHandler> webSocketClientHandlerList) {
        this.channelHandlerContext2WebSocketClientHandlerMap = channelHandlerContext2WebSocketClientHandlerMap;
        this.webSocketClientHandlerList = webSocketClientHandlerList;
    }

    @Override
    public void channelRead(ChannelHandlerContext ctx, Object msg) {
        if (msg instanceof TextWebSocketFrame) {
            TextWebSocketFrame textWebSocketFrame = (TextWebSocket
