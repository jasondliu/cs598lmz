import io.netty.channel.ChannelHandlerContext;
import io.netty.channel.SimpleChannelInboundHandler;
import io.netty.channel.group.ChannelGroup;
import io.netty.channel.group.DefaultChannelGroup;
import io.netty.handler.codec.http.websocketx.TextWebSocketFrame;
import io.netty.util.concurrent.GlobalEventExecutor;

/**
 * 
 * @author zhangchao
 * @date 2018年6月12日 下午1:47:46
 * @Description: TextWebSocketFrame:在netty中，使用了websocket之后，传输的数据都是以frame形式进行传输的
 */
public class ChatHandler extends SimpleChannelInboundHandler<TextWebSocketFrame> {
	
	//用于记录和管理所有客户端的channel
	private static ChannelGroup
