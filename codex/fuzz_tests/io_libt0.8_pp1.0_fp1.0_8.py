import io.netty.channel.EventLoopGroup;
import io.netty.channel.nio.NioEventLoopGroup;
import io.netty.channel.socket.SocketChannel;
import io.netty.channel.socket.nio.NioServerSocketChannel;
import io.netty.handler.codec.LineBasedFrameDecoder;
import io.netty.handler.codec.string.StringDecoder;
import io.netty.handler.codec.string.StringEncoder;
import io.netty.util.CharsetUtil;

import java.util.Timer;
import java.util.TimerTask;

/**
 * Netty服务端代码
 * @author yangtao__anxpp.com
 * @version 1.0
 */
public class NettyServerBootstrap {
	private int port;
	private SocketChannel socketChannel;
	public NettyServerBootstrap(int port) throws InterruptedException{
		this.port = port;
		bind();
		Timer timer = new Timer();
	
