import io.netty.channel.SimpleChannelInboundHandler;
import io.netty.channel.socket.SocketChannel;
import io.netty.util.AttributeKey;
import io.netty.util.ReferenceCountUtil;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;

import java.util.Map;

/**
 * @author: wangsaichao
 * @date: 2019/1/19
 * @description: 处理业务逻辑
 */
@Slf4j
@ChannelHandler.Sharable
public class NettyServerHandler extends SimpleChannelInboundHandler<Packet> {

    /**
     * 管理所有的channel
     */
    @Autowired
    private ChannelGroup channelGroup;

    /**
     * 消息处理器
     */
    @Autowired
    private Map<String, SimpleChannelInboundHandler<? extends Packet>> handlerMap;
