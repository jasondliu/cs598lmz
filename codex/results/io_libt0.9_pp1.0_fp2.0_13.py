import io.netty.handler.codec.http.HttpHeaderNames.SET_COOKIE;
import static io.netty.handler.codec.http.HttpHeaderNames.SET_COOKIE2;
import static io.netty.handler.codec.http.HttpHeaderValues.TEXT_PLAIN;
import static io.netty.handler.codec.http.HttpResponseStatus.BAD_REQUEST;
import static io.netty.handler.codec.http.HttpResponseStatus.FORBIDDEN;

import org.dancres.http.ContentTypes;
import org.dancres.http.Handler;
import org.dancres.http.PostHandler;
import org.dancres.http.Session.Attributes;

import com.sun.istack.NotNull;

/**
 * Provides administration services for the data service. Currently supports
 * maintainance via a console view of the arena.
 *
 * @see ArenaViewHandler
 */
public class AdminHandler implements Handler, PostHandler {
	private static final String ADMIN = "/admin";

	private static final String LOGIN
