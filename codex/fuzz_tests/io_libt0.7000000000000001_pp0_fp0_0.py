import io.netty.buffer.ByteBuf;
import net.minecraft.client.Minecraft;
import net.minecraft.entity.player.EntityPlayer;
import net.minecraft.entity.player.EntityPlayerMP;
import net.minecraft.nbt.NBTTagCompound;
import net.minecraft.server.MinecraftServer;
import net.minecraft.util.text.TextComponentTranslation;
import net.minecraftforge.fml.common.network.simpleimpl.IMessage;
import net.minecraftforge.fml.common.network.simpleimpl.IMessageHandler;
import net.minecraftforge.fml.common.network.simpleimpl.MessageContext;
import net.minecraftforge.fml.relauncher.Side;

public class PacketClericSetAbility extends LMPacket<PacketClericSetAbility> {

    private int ability;

    public PacketClericSetAbility(int ability){
        this.ability = ability;
    }

    public PacketClericSetAbility() {
    }

    @Override
    public void toBytes(ByteBuf buf) {
        buf.writeInt(
