import io.netty.channel.ChannelHandlerContext;
import io.netty.handler.codec.MessageToMessageEncoder;
import lombok.extern.slf4j.Slf4j;


@Slf4j
public class BlackIPEncoder extends MessageToMessageEncoder<AppBlackIP> {

    @Override
    protected void encode(ChannelHandlerContext channelHandlerContext, AppBlackIP appBlackIP, List<Object> list) throws Exception {
        log.info("返回到客户端的信息为："+appBlackIP.toString());
        byte[] bytes = SerializationUtils.serialize(appBlackIP);
        list.add(bytes);
    }
}
