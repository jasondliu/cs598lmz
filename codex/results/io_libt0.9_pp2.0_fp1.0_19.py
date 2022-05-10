import io.netty.channel.ChannelFuture;
import io.netty.channel.ChannelInboundHandlerAdapter;
import io.netty.channel.ChannelInitializer;
import io.netty.channel.nio.NioEventLoopGroup;
import io.netty.channel.socket.nio.NioServerSocketChannel;
import io.netty.channel.socket.nio.NioSocketChannel;

/**
 * @author lengguanglong
 * @title: Server
 * @projectName demo
 * @description: TODO
 * @date 2020/2/25 11:41
 */
public class Server {

    public static void main(String[] args) {
        //准备一个线程池
        NioEventLoopGroup bossGroup = new NioEventLoopGroup();
        NioEventLoopGroup workerGroup = new NioEventLoopGroup();

        //创建监听线程
        ServerBootstrap serverBootstrap = new ServerBootstrap();
        //指定线程
