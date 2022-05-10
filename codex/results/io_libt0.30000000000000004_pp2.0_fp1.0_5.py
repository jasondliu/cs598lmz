import io.netty.handler.codec.http.HttpResponse;
import io.netty.handler.codec.http.HttpResponseStatus;
import io.netty.handler.codec.http.HttpVersion;
import io.netty.util.CharsetUtil;

/**
 * @author zhangjianbin
 *
 */
public class HttpServerHandler extends SimpleChannelInboundHandler<FullHttpRequest> {

	private static final Logger logger = LoggerFactory.getLogger(HttpServerHandler.class);

	private static final String WEB_ROOT = "webroot";

	private static final String FAVICON_ICO = "/favicon.ico";

	private static final String HTTP_DATE_FORMAT = "EEE, dd MMM yyyy HH:mm:ss zzz";

	private static final String HTTP_DATE_GMT_TIMEZONE = "GMT";

	private static final int HTTP_CACHE_SECONDS = 60;

	private static final String HTTP_CONTENT_TYPE_TEXT_HTML = "text/html; charset=UTF-
