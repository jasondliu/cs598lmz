import io.netty.buffer.ByteBuf;
+import net.minecraft.network.NetHandlerPlayServer;
+import java.io.IOException;
+
+public class C12PlayerLook implements Packet<NetHandlerPlayServer> {
+
+    private float yaw;
+    private float pitch;
+    private boolean onGround;
+
+    public C12PlayerLook() {
+    }
+
+    public C12PlayerLook(float yaw, float pitch, boolean onGround) {
+        this.yaw = yaw;
+        this.pitch = pitch;
+        this.onGround = onGround;
+    }
+
+    @Override
+    public void decode(ByteBuf buf) throws IOException {
+        this.yaw = buf.readFloat();
+        this.pitch = buf.readFloat();
+        this.onGround = buf.readByte() != 0;
+    }
+
+    @Override
+    public void encode(ByteBuf buf) throws IOException {
+        buf.writeFloat(this
