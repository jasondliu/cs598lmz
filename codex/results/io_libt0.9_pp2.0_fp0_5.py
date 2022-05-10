import io.netty.handler.ssl.SslContext;
import io.netty.handler.ssl.SslContextBuilder;
import io.netty.handler.ssl.SslHandler;
import io.netty.handler.stream.ChunkedWriteHandler;

import javax.net.ssl.SSLException;
import java.io.File;
import java.io.IOException;
import java.net.URL;

/**
 * @author zhangwentao02
 */
public class HttpsServer {
    public static void main(String[] args) throws Exception {
        // Configure SSL.
        URL url = Resources.getResource("server.jks");
        File serverCertChainFile = new File(url.getFile());
        SslContext sslCtx = SslContextBuilder.forServer(serverCertChainFile, serverCertChainFile)
                .build();

        // Configure the server.
        EventLoopGroup bossGroup = new NioEventLoopGroup(1);
        EventLoopGroup workerGroup = new NioEventLoopGroup();
        try {
            Server
