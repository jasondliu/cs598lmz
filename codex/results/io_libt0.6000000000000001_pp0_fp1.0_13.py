import io.netty.buffer.ByteBuf;
import io.netty.channel.ChannelHandlerContext;
import io.netty.handler.codec.ByteToMessageDecoder;
import io.netty.handler.codec.CorruptedFrameException;
import io.netty.util.AttributeKey;

import java.util.List;

public class MqttDecoder extends ByteToMessageDecoder {

    private final AttributeKey<Boolean> ATTR_KEY_MQTT_CONNACK_RECEIVED = AttributeKey.valueOf("mqtt.CONNACK.received");
    private final AttributeKey<Integer> ATTR_KEY_MQTT_CONNACK_RESULT = AttributeKey.valueOf("mqtt.CONNACK.returnCode");
    private final AttributeKey<Integer> ATTR_KEY_MQTT_CONNACK_SESSION_PRESENT = AttributeKey.valueOf("mqtt.CONNACK.sessionPresent");

    @Override
    protected void decode(ChannelHandlerContext ctx, ByteBuf in, List<Object> out
