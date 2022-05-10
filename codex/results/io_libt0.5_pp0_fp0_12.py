import io.vertx.ext.web.handler.sockjs.SockJSHandler;
import io.vertx.ext.web.handler.sockjs.SockJSSocket;
import io.vertx.ext.web.sstore.LocalSessionStore;
import io.vertx.ext.web.sstore.SessionStore;
import io.vertx.servicediscovery.Record;
import io.vertx.servicediscovery.ServiceDiscovery;
import io.vertx.servicediscovery.ServiceDiscoveryOptions;
import io.vertx.servicediscovery.types.EventBusService;
import io.vertx.servicediscovery.types.HttpEndpoint;
import io.vertx.servicediscovery.types.MessageSource;
import io.vertx.servicediscovery.types.TCPEndpoint;
import io.vertx.servicediscovery.types.WebsocketEndpoint;
import io.vertx.servicediscovery.types.WebsocketMessageSource;

public class WebServerVerticle extends AbstractVerticle {

	private static final Logger LOGGER = LoggerFactory
