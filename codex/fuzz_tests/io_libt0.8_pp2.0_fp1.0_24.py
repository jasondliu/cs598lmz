import io.netty.buffer.ByteBuf;
import net.minecraft.network.PacketBuffer;
import net.minecraft.util.math.BlockPos;
import net.minecraftforge.fml.network.NetworkEvent;
import net.minecraftforge.fml.network.PacketDistributor;
import org.apache.logging.log4j.LogManager;

import java.util.function.Supplier;

public class S2CSyncCablePos {

    private int posX = 0;
    private int posY = 0;
    private int posZ = 0;

    public S2CSyncCablePos(BlockPos pos) {
        this.posX = pos.getX();
        this.posY = pos.getY();
        this.posZ = pos.getZ();
    }

    public static void encode(S2CSyncCablePos msg, PacketBuffer buffer) {
        buffer.writeInt(msg.posX);
        buffer.writeInt(msg.posY);
        buffer.writeInt(msg.posZ);
    }

    public static S2
