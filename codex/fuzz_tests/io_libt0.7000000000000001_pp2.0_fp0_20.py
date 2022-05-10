import io.netty.channel.ChannelHandlerContext;
import io.netty.channel.SimpleChannelInboundHandler;

public class RPCClientHandler extends SimpleChannelInboundHandler<Message> {

    // 消息回复
    private Message messageResponse;

    public Message getMessageResponse() {
        return messageResponse;
    }

    @Override
    protected void channelRead0(ChannelHandlerContext channelHandlerContext, Message message)
            throws Exception {
        this.messageResponse = message;
    }

    @Override
    public void exceptionCaught(ChannelHandlerContext ctx, Throwable cause) throws Exception {
        System.out.println("client exception is general");
    }
}
