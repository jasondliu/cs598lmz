import io.netty.channel.socket.SocketChannel;
import io.netty.channel.socket.nio.NioSocketChannel;

/**
 * @author emininal
 * @since 27.07.2020
 */
public class Client {

  public static void main(String[] args) throws Exception {
    EventLoopGroup group = new NioEventLoopGroup();

    try {
      Bootstrap b = new Bootstrap();
      b.group(group)
          .channel(NioSocketChannel.class)
          .option(ChannelOption.TCP_NODELAY, true)
          .handler(new ChannelInitializer<SocketChannel>() {
            @Override
            public void initChannel(SocketChannel ch) {
              ChannelPipeline p = ch.pipeline();
              p.addLast(new ProtobufVarint32FrameDecoder());
              p.addLast(new ProtobufDecoder(SearchResponse.SearchResponseMessage.getDefaultInstance()));

              p.addLast(new ProtobufVarint32LengthFieldPrepender());
              p.addLast(new Protobuf
