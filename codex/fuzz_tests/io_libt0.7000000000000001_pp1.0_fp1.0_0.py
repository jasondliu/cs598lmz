import io.netty.channel.ChannelHandler;
import io.netty.channel.ChannelHandlerContext;
import io.netty.channel.ChannelPipeline;
import io.netty.handler.codec.http.HttpRequestDecoder;
import io.netty.handler.codec.http.HttpResponseEncoder;
import io.netty.handler.ssl.SslHandler;

import javax.net.ssl.SSLEngine;

public abstract class WebSocketServer extends WebServer {
    protected String webSocketPath;

    public WebSocketServer(String serverName, int port, String webSocketPath) {
        super(serverName, port);
        this.webSocketPath = webSocketPath;
    }

    @Override
    protected ChannelHandler getChildHandler() {
        return new WebSocketServerInitializer(webSocketPath, sslContext);
    }

    public static class WebSocketServerInitializer extends ChannelInitializer<SocketChannel> {
        private String webSocketPath;
        private SslContext sslContext;

        public WebSocketServerInitializer(String webSocketPath,
