import io.netty.buffer.ByteBuf;
import io.netty.channel.ChannelHandler;
import io.netty.channel.ChannelHandlerContext;
import io.netty.handler.codec.MessageToByteEncoder;
import io.netty.util.AttributeKey;
import net.machinemuse.general.MuseLogger;
import net.machinemuse.numina.network.MusePacket;
import org.apache.logging.log4j.Level;

import java.io.IOException;
import java.net.SocketAddress;
import java.util.HashMap;
import java.util.Map;

@ChannelHandler.Sharable
public class MusePacketEncoder extends MessageToByteEncoder<MusePacket> {
    public static final AttributeKey<Map<Class<? extends MusePacket>, Integer>> PACKET_ID_MAP = AttributeKey.valueOf("net.machinemuse.powersuits.network.MusePacketEncoder.PACKET_ID_MAP");
    public static final int MAX_PACKET_SIZE =
