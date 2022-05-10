import io.netty.channel.socket.nio.NioServerSocketChannel;
+import io.netty.handler.logging.LogLevel;
+import io.netty.handler.logging.LoggingHandler;
+
+/**
+ * @Auther ChenShuHong
+ * @Date 2020-08-23 14:22
+ * @Description
+ */
+public class MyServer {
+  public static void main(String[] args) throws Exception {
+    //1.创建一个线程组
+    EventLoopGroup bossGroup = new NioEventLoopGroup(1);
+    //2.创建一个线程组 用于处理客户端的数据 读写操作
+    EventLoopGroup workGroup = new NioEventLoopGroup();
+    //3.创建服务器端启动助手 来自动
