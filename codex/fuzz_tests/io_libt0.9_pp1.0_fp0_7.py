import io.netty.buffer.ByteBuf;
import net.minecraft.nbt.NBTTagCompound;
import net.minecraft.network.PacketBuffer;

public class NBTByteBufUtil {
  public static byte[] readBlob(ByteBuf buf) throws IOException {
    int length = buf.readInt();
    byte[] bytes = new byte[length];
    buf.readBytes(bytes);
    return bytes;
  }

  public static void writeBlob(ByteBuf buf, byte[] bytes) throws IOException {
    buf.writeInt(bytes.length);
    buf.writeBytes(bytes);
  }

  public static void writeNBT(ByteBuf buf, NBTTagCompound tag) throws IOException {
    PacketBuffer packetBuf = new PacketBuffer(buf);
    packetBuf.writeCompoundTag(tag);
  }

  public static NBTTagCompound readNBT(ByteBuf buf) throws IOException {
    PacketBuffer packetBuf = new PacketBuffer(buf);
    return packetBuf.readComp
