import io.netty.channel.EventLoopGroup;
import io.netty.channel.nio.NioEventLoopGroup;
import io.netty.channel.socket.SocketChannel;
import io.netty.channel.socket.nio.NioSocketChannel;

import java.net.InetSocketAddress;

/**
 * Chat Server Client
 *
 * @since 2019-01-03
 * @author colg
 */
public class ChatServerClient {

    private EventLoopGroup group;
    private Bootstrap bootstrap;

    public ChatServerClient() {
        group = new NioEventLoopGroup();
        bootstrap = new Bootstrap();
        bootstrap.group(group)
                 .channel(NioSocketChannel.class)
                 .handler(new ChannelInitializer<SocketChannel>() {
                     @Override
                     protected void initChannel(SocketChannel ch) throws Exception {
                         ch.pipeline().addLast(new FirstClientHandler());
                     }
                 });
    }

    public void run() {
        ChannelFuture channelFuture = bootstrap.connect(new InetSocketAddress("
