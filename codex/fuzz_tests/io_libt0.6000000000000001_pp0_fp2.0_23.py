import io.netty.channel.ChannelHandlerContext;
import io.netty.handler.ssl.ApplicationProtocolNames;
import io.netty.handler.ssl.ApplicationProtocolNegotiationHandler;
import io.netty.handler.ssl.SslContext;
import io.netty.util.AsciiString;

public class Http2OrHttpHandler extends ApplicationProtocolNegotiationHandler {

    private static final AsciiString HTTP_1_1 = AsciiString.cached("HTTP/1.1");
    private static final AsciiString HTTPS = AsciiString.cached("https");

    private final SslContext sslContext;
    private final boolean startHttp2;
    private final boolean startWebSocket;
    private final boolean startHttp;

    public Http2OrHttpHandler(SslContext sslContext, boolean startHttp2, boolean startWebSocket,
                              boolean startHttp) {
        super(ApplicationProtocolNames.HTTP_1_1);
        this.sslContext = sslContext;
        this.startHttp2 = startHttp2;
        this.
