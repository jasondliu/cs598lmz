import io.netty.buffer.ByteBuf;
import net.minecraft.entity.player.EntityPlayer;
import net.minecraft.util.math.BlockPos;
import net.minecraftforge.fml.common.network.ByteBufUtils;
import net.minecraftforge.fml.common.network.simpleimpl.IMessage;
import net.minecraftforge.fml.common.network.simpleimpl.IMessageHandler;
import net.minecraftforge.fml.common.network.simpleimpl.MessageContext;
import net.minecraftforge.fml.relauncher.Side;

public class MessageCraftingGoods implements IMessage {
	
	private BlockPos pos;
	private String name;
	private boolean isCraftingGoods;
	
	public MessageCraftingGoods() {
		
	}
	
	public MessageCraftingGoods(BlockPos pos, String name, boolean isCraftingGoods) {
		this.pos = pos;
		this.name = name;
		this.isCraftingGoods = isCraftingGoods;
	}

	@Override
	public
