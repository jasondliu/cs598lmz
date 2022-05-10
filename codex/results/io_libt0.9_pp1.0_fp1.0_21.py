import io.netty.channel.ChannelHandlerContext;
+import io.netty.channel.SimpleChannelInboundHandler;
+import io.netty.util.ReferenceCountUtil;
+
+/**
+ * @author xie
+ * @date 2020/5/5 21:07
+ */
+public class ClientHandler extends SimpleChannelInboundHandler<ByteBuf> {
+
+    @Override
+    public void exceptionCaught(ChannelHandlerContext ctx, Throwable cause) throws Exception {
+        System.out.println("服务端异常！" + cause);
+    }
+
+    @Override
+    protected void channelRead0(ChannelHandlerContext ctx, ByteBuf msg) throws Exception {
+
+        try {
+            byte[] buffer = new byte[msg.readableBytes()];
+            msg.readBytes(buffer);
+            String message = new String(buffer, "UTF-8");
+
+            System.out.println("客户端收到消息 = "
