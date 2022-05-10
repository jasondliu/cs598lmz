import io.netty.util.concurrent.Future;
import io.netty.util.concurrent.GenericFutureListener;

public class TestClient {
	public static void main(String[] args) throws InterruptedException, ExecutionException {
		String host = "127.0.0.1";
		int port = 8080;
		
		EventLoopGroup workerGroup = new NioEventLoopGroup();
		
		try {
			Bootstrap b = new Bootstrap();
			b.group(workerGroup);
			b.channel(NioSocketChannel.class);
			b.option(ChannelOption.SO_KEEPALIVE, true);
			b.handler(new ChannelInitializer<SocketChannel>() {

				@Override
				protected void initChannel(SocketChannel ch) throws Exception {
					ch.pipeline().addLast(new TestClientHandler());
				}
			});
			
			// 发起异步
