import io.netty.channel.EventLoopGroup;
import io.netty.channel.nio.NioEventLoopGroup;
import io.netty.channel.socket.nio.NioSocketChannel;

/**
 * @Author: Lake
 * @Date: 2019/7/8 11:46
 * @Description: client实体类
 */
public class NettyClient extends Thread{

    private final String host;
    private final int port;
    private final long time;

    NettyClient(String host, int port, long time){
        this.host = host;
        this.port = port;
        this.time = time;
    }

    @Override
    public void run(){
        // 首先，netty通过ServerBootstrap启动服务端
        EventLoopGroup group = new NioEventLoopGroup();
        Bootstrap b = new Bootstrap();
        b.group(group)
                //指定所使用的 NIO 传输 Channel
                .channel
