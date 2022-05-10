import io.netty.channel.ChannelHandlerContext;
import io.netty.channel.ChannelInboundHandlerAdapter;
import io.netty.handler.timeout.IdleState;
import io.netty.handler.timeout.IdleStateEvent;
import io.netty.util.ReferenceCountUtil;

import java.util.Date;

/**
 * @author luoyong
 * @Description: NettyClientHandler
 * @create 2019-12-26 22:05
 * @last modify by [LuoYong 2019-12-26 22:05]
 **/
public class NettyClientHandler extends ChannelInboundHandlerAdapter {

    /**
     * @param ctx
     * @param msg
     * @return void
     * @Description: 当通道有读取事件时，会触发
     * @author luoyong
     * @create 22:07 2019/12/26
     * @last modify by [LuoYong 22:07 2019/12/26 ]
     */
    @Override
