import io.netty.bootstrap.Bootstrap;
+import io.netty.buffer.ByteBuf;
+import io.netty.buffer.Unpooled;
+import io.netty.channel.ChannelFuture;
+import io.netty.channel.ChannelInitializer;
+import io.netty.channel.EventLoopGroup;
+import io.netty.channel.nio.NioEventLoopGroup;
+import io.netty.channel.socket.SocketChannel;
+import io.netty.channel.socket.nio.NioSocketChannel;
+import io.netty.handler.codec.DelimiterBasedFrameDecoder;
+import io.netty.handler.codec.string.StringDecoder;
+
+/**
+ * @author <a href="mailto:liaochunyhm@live.com">liaochuntao</a>
+ * @since 0.0.1
+ */
+public class EchoClient {
+
+    private final String host;
+    private final int port;
+
+    private ChannelFuture future;
