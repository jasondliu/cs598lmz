import io.netty.channel.ChannelInitializer;
import io.netty.channel.EventLoopGroup;
import io.netty.channel.nio.NioEventLoopGroup;
import io.netty.channel.socket.SocketChannel;
import io.netty.channel.socket.nio.NioServerSocketChannel;

import java.util.ArrayList;
import java.util.List;

public class Server {
	
	public static void main(String[] args) {
		new Server().start();
	}
	
	private List<Channel> channels = new ArrayList<Channel>();
	
	public List<Channel> getChannels(){
		return channels;
	}
	
	public void start(){
		
		EventLoopGroup boss = new NioEventLoopGroup();
		EventLoopGroup worker = new NioEventLoopGroup();
		
		ServerBootstrap sb = new ServerBootstrap();
		sb.group(boss, worker);
		sb.channel(NioServerSocketChannel.class);
		sb.childHandler
