import io.netty.handler.codec.http.HttpHeaderValues;
import io.netty.handler.codec.http.HttpHeaders;
import io.netty.handler.codec.http.HttpRequest;
import io.netty.handler.codec.http.HttpResponse;
import io.netty.handler.codec.http.HttpResponseStatus;
import io.netty.util.AttributeKey;
import io.netty.util.concurrent.GenericFutureListener;

public class HttpServerHandler extends SimpleChannelInboundHandler<FullHttpRequest> {
	
	public static final AttributeKey<Session> SESSION_KEY = AttributeKey.valueOf("session");
	private static final String FILTER_CHAIN_FACTORY = "filterChainFactory";
	private static final String CONTROLLER = "controller";
	private static final String CONTEXT = "context";
	private static final String ERROR_HANDLER = "errorHandler";
	private static final String STATIC_RESOURCE = "staticResource";
	private static final String WEBSOCKET = "websocket";
