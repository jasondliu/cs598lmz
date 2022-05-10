import io.vertx.core.Vertx;
import io.vertx.core.http.HttpServer;
import io.vertx.core.http.HttpServerOptions;
import io.vertx.core.http.ServerWebSocket;
import io.vertx.core.json.Json;
import io.vertx.ext.web.Router;
import io.vertx.ext.web.RoutingContext;
import io.vertx.ext.web.handler.sockjs.BridgeOptions;
import io.vertx.ext.web.handler.sockjs.PermittedOptions;
import io.vertx.ext.web.handler.sockjs.SockJSHandler;

public class VertxServer {
	private static final Logger log = LogManager.getLogger(VertxServer.class);
	private static final String SOCK_ADDRESS = "sock.address";

	public static void main(String[] args) {
		Vertx vertx = Vertx.vertx();

		HttpServer server = vertx.createHttpServer(new HttpServerOptions
