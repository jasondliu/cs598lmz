import io.netty.channel.socket.SocketChannel;
import io.netty.handler.codec.http.HttpRequestDecoder;
import io.netty.handler.codec.http.HttpResponseEncoder;

public class HelloServerInitializer extends ChannelInitializer<SocketChannel> {
    @Override
    protected void initChannel(SocketChannel socketChannel) throws Exception {
        // server端发送的是httpResponse，所以要使用HttpResponseEncoder进行编码
        socketChannel.pipeline().addLast(new HttpResponseEncoder());
        // server端接收到的是httpRequest，所以要使用HttpRequestDecoder进行解码
        socketChannel.pipeline().addLast(new HttpRequestDecoder());
        // 业务逻辑
        socketChannel.pipeline().addLast(new HelloServerHandler());
    }
}
