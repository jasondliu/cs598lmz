import io.vertx.core.http.HttpServerRequest;
import io.vertx.core.json.JsonObject;
import io.vertx.core.logging.Logger;
import io.vertx.core.logging.LoggerFactory;
import io.vertx.ext.web.Router;
import io.vertx.ext.web.RoutingContext;
import io.vertx.ext.web.handler.BodyHandler;
import io.vertx.ext.web.handler.CorsHandler;
import io.vertx.ext.web.handler.StaticHandler;

/**
 * Created by koushikkrishnan on 9/15/16.
 */
public class HttpServer extends AbstractVerticle {
    public static final String HTTP_SERVER_PORT = "http.server.port";
    public static final String HTTP_SERVER_HOST = "http.server.host";
    public static final String CORS_ALLOWED_ORIGIN = "cors.allowed.origin";
    private static final Logger LOGGER = LoggerFactory.getLogger(HttpServer
