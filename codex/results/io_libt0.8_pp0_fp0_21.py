import io.netty.channel.socket.nio.NioSocketChannel;
import io.netty.handler.codec.LengthFieldBasedFrameDecoder;
import io.netty.handler.codec.LengthFieldPrepender;
import io.netty.handler.codec.string.StringDecoder;
import io.netty.handler.codec.string.StringEncoder;
import io.netty.util.CharsetUtil;

/**
 * @author: faker
 * @date: 2020/5/6 10:49 上午
 */
public class MyClient {
    public static void main(String[] args) throws InterruptedException {
        //创建客户端处理器
        EventLoopGroup group = new NioEventLoopGroup();
        //创建客户端启动对象
        Bootstrap bootstrap = new Bootstrap();
        //设置服务参数
        bootstrap.group(group)
                .channel(N
