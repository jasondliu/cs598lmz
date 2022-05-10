import io.netty.channel.ChannelOption;
import io.netty.channel.EventLoopGroup;
import io.netty.channel.nio.NioEventLoopGroup;
import io.netty.channel.socket.nio.NioServerSocketChannel;
import io.netty.handler.logging.LogLevel;
import io.netty.handler.logging.LoggingHandler;

/**
 * @author: huangyibo
 * @Date: 2019/3/8 23:02
 * @Description:
 *
 * 使用Netty实现Http文件服务器
 */
public class HttpFileServer {

    private static final String DEFAULT_URL = "/src/main/java/com/hyb/chapter03/";

    public void run(final int port,final String url) throws Exception{
        EventLoopGroup bossGroup = new NioEventLoopGroup();
        EventLoopGroup workerGroup = new NioEventLoopGroup();
        try {
            ServerBootstrap b = new ServerBootstrap();
            b.group(
