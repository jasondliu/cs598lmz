import io.netty.handler.codec.MessageToMessageDecoder;
import io.netty.handler.codec.http.websocketx.TextWebSocketFrame;

import java.util.List;

import com.zdy.common.util.JsonUtils;
import com.zdy.common.util.SpringContextUtil;
import com.zdy.dubbo.api.service.log.IUserLogService;
import com.zdy.dubbo.common.util.BaseList;
import com.zdy.dubbo.model.log.UserLog;
import com.zdy.dubbo.web.controller.log.vo.UserLogReq;
import com.zdy.dubbo.web.controller.log.vo.UserLogResp;


public class UserLogDecoder extends MessageToMessageDecoder<TextWebSocketFrame>{
	
	@Override
	protected void decode(ChannelHandlerContext ctx, TextWebSocketFrame msg,
			List<Object> out) throws Exception {
		System.out.println(msg.
