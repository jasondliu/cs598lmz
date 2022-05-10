import io.netty.channel.ChannelHandlerContext;

import java.util.logging.Logger;

/**
 * @author xielongwang
 * @create 2019-03-22 下午4:54
 * @email xielong.wang@nvr-china.com
 * @description
 */
public class SubReqClientHandler extends ChannelHandlerAdapter{
    private static final Logger logger = Logger.getLogger(SubReqClientHandler.class.getName());

    public SubReqClientHandler() {
    }

    @Override
    public void channelActive(ChannelHandlerContext ctx) throws Exception {
        for (int i = 0; i < 10; i++) {
            ctx.write(subReq(i));
        }
        ctx.flush();
    }

    private SubscribeReqProto.SubscribeReq subReq(int i) {
        SubscribeReqProto.SubscribeReq.Builder builder = SubscribeReqProto.SubscribeReq.newBuilder();
        builder.setSubReqID(i);
        builder.setUser
