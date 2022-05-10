import io.netty.channel.group.ChannelGroup;
import io.netty.channel.group.DefaultChannelGroup;
import io.netty.util.concurrent.GlobalEventExecutor;

public class ChannelUtil {

	private static final ChannelGroup CHANNEL_GROUP;

	static {
		CHANNEL_GROUP = new DefaultChannelGroup(GlobalEventExecutor.INSTANCE);
	}

	public static ChannelGroup getChannelGroup() {
		return CHANNEL_GROUP;
	}
}
