import io.netty.channel.ChannelOption;
import io.netty.channel.nio.NioEventLoopGroup;
import io.netty.channel.socket.nio.NioServerSocketChannel;
import io.netty.channel.socket.nio.NioSocketChannel;
import io.netty.util.AttributeKey;
import io.netty.util.concurrent.Future;
import io.netty.util.concurrent.GenericFutureListener;

import java.util.Date;

public class NettyServer {

    public static void main(String[] args) {
        // 创建两个线程组
        // 接收客户端的TCP连接，但是不做任何处理
        NioEventLoopGroup bossGroup = new NioEventLoopGroup();
        // 负责处理每一条连接的数据读写
        Nio
