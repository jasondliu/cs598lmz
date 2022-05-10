import io.netty.handler.codec.http.HttpResponseStatus;
import io.netty.util.CharsetUtil;

public class HttpJsonResponseEncoder extends AbstractHttpJsonEncoder<HttpJsonResponse> {

	@Override
	protected void encode(ChannelHandlerContext ctx, HttpJsonResponse msg, List<Object> out) throws Exception {
		ByteBuf body = encode0(ctx, msg.getResult());
		FullHttpResponse response = msg.getHttpResponse();
		if(response == null){
			response = new DefaultFullHttpResponse(HttpVersion.HTTP_1_1, HttpResponseStatus.OK, body);
		}else{
			response = new DefaultFullHttpResponse(msg.getHttpResponse().protocolVersion(), msg.getHttpResponse().status(), body);
		}
		response.headers().set(HttpHeaderNames.CONTENT_TYPE, "text/json");
		HttpUtil.setContentLength(response, body.readableBytes());
		out.add(response);
	}

	
