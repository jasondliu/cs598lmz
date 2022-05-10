import io.netty.channel.socket.SocketChannel;
import io.netty.channel.socket.nio.NioSocketChannel;
import io.netty.util.AttributeKey;

/**
 * @author wangshuai
 * @version V1.0
 * @date 2018-06-25 17:01
 */
public class Client {

    private static final AttributeKey<SocketChannel> CLIENT_KEY = AttributeKey.newInstance("clientKey");

    public static void main(String[] args) throws InterruptedException {
        EventLoopGroup group = new NioEventLoopGroup();
        Bootstrap bootstrap = new Bootstrap();
        bootstrap.group(group)
                .channel(NioSocketChannel.class)
                .handler(new ChannelInitializer<SocketChannel>() {
                    @Override
                    protected void initChannel(SocketChannel ch) throws Exception {
                        ch.pipeline().addLast(new ClientHandler());
                    }
                });

        ChannelFuture future = bootstrap.connect("localhost", 8888).sync();
        future.channel().writeAndFlush("Hello Netty
