import io.netty.channel.socket.nio.NioServerSocketChannel;
import io.netty.handler.codec.string.StringDecoder;
import io.netty.handler.codec.string.StringEncoder;

/**
 * @author ddnosh
 * @website http://blog.csdn.net/ddnosh
 */
public class SimpleServer {

    public static void main(String[] args) {
        ServerBootstrap server = new ServerBootstrap();
        EventLoopGroup boss = new NioEventLoopGroup();
        EventLoopGroup work = new NioEventLoopGroup();
        try {
            server.group(boss, work)
                    .channel(NioServerSocketChannel.class)
                    .childHandler(new SimpleServerInitializer());

            ChannelFuture sync = server.bind(8899).sync();
            sync.channel().closeFuture().sync();

        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            boss.shutdownGracefully();
            work.shutdownGracefully();
        }
    }

