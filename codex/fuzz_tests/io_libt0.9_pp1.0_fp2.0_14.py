import io.netty.channel.ChannelHandlerContext;
import java.util.Set;
import protocolsupport.api.events.ServerPingResponseEvent;
import protocolsupport.protocol.packet.middle.ServerBoundMiddlePacket;
import protocolsupport.protocol.serializer.ProtocolSupportPacketDataSerializer;
import protocolsupport.protocol.storage.netcache.Attributes;
import protocolsupport.protocol.utils.authlib.SkinData;

public abstract class MiddleServerInfoRequest<T> extends ServerBoundMiddlePacket<T> {

	protected ProtocolSupportPacketDataSerializer serializer;

	@Override
	protected void readServerData(ProtocolSupportPacketDataSerializer serializer) {
		this.serializer = serializer;
	}

	@Override
	public void handle() {
		Channel channel = connection.getChannel();
		ChannelHandlerContext handlerContext = channel.pipeline().firstContext();
		ServerPingResponseEvent event = new ServerPingResponseEvent(
			StringUtils.clamp(serializer.readString(40), connection.getVersion().get
