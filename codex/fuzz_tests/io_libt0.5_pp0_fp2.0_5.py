import io.netty.channel.ChannelHandlerContext;
import io.netty.channel.SimpleChannelInboundHandler;
import io.netty.handler.codec.http.FullHttpResponse;

/**
 * @author luomeng
 * @date 2018/11/5
 */
public class HttpClientInboundHandler extends SimpleChannelInboundHandler<FullHttpResponse> {
    @Override
    protected void channelRead0(ChannelHandlerContext ctx, FullHttpResponse msg) throws Exception {
        System.out.println("client receive response of http header is : " + msg.headers().names());
        System.out.println("client receive response of http body is : " + msg.content().toString(CharsetUtil.UTF_8));
    }
}
