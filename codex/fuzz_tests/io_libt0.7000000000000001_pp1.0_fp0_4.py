import io.netty.channel.socket.nio.NioSocketChannel;

public class HttpClient {
    public static void main(String[] args) throws Exception{
        Bootstrap bootstrap = new Bootstrap();
        NioEventLoopGroup group = new NioEventLoopGroup();

        bootstrap.group(group).channel(NioSocketChannel.class).handler(new HttpClientInitializer());

        Channel ch = bootstrap.connect("127.0.0.1", 8080).channel();

        HttpRequest request = new DefaultHttpRequest(HttpVersion.HTTP_1_1, HttpMethod.GET, "http://127.0.0.1:8080");
        request.headers().add(HttpHeaderNames.HOST, "127.0.0.1");
        request.headers().add(HttpHeaderNames.CONNECTION, HttpHeaderValues.KEEP_ALIVE);
        request.headers().add(HttpHeaderNames.CONTENT_LENGTH, request.content().readableBytes());

        ch.writeAndFlush(request);
        ch.closeFuture().sync();

    }
