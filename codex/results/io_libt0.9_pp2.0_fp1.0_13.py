import io.vertx.core.http.HttpHeaders;
import io.vertx.core.json.JsonObject;
import io.vertx.ext.web.Router;
import io.vertx.ext.web.RoutingContext;
import io.vertx.ext.web.handler.BodyHandler;
import io.vertx.ext.web.handler.CorsHandler;
import io.vertx.ext.web.handler.StaticHandler;

public class MainVerticle extends AbstractVerticle {

	private static final String HOST = "0.0.0.0";
	private static final int PORT = 8080;

	private final Logger logger = LoggerFactory.getLogger(MainVerticle.class);

	@Override
    public void start(Future<Void> startFuture) throws Exception {

		Router router = Router.router(vertx);

		registerRoute(router);

		vertx
        .createHttpServer()
        .requestHandler(router::accept)
        .listen(
            // Retrieve the port from the configuration, default
