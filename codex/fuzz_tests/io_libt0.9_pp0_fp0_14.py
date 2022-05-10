import io.netty.handler.codec.LengthFieldPrepender;

public class EchoServer {
	public void run(int port) throws Exception
	{
		EventLoopGroup bossGroup=new NioEventLoopGroup();
		EventLoopGroup workerGroup=new NioEventLoopGroup();
		try{
			ServerBootstrap b=new ServerBootstrap();
			b.group(bossGroup, workerGroup)
			 .channel(NioServerSocketChannel.class)
			 .childHandler(new ChannelInitializer<SocketChannel>() {
				protected void initChannel(SocketChannel ch) throws Exception{
					ch.pipeline().addLast(new LengthFieldBasedFrameDecoder(65535, 0, 2,0,
							2));
					ch.pipeline().addLast(new MessagePackDecoder());
					ch.pipeline().addLast(new LengthFieldPrepender(2));
					ch.pipeline().addLast(new MessagePackEnc
