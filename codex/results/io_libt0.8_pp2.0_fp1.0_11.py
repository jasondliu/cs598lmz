import io.vertx.core.buffer.Buffer;
import io.vertx.core.json.JsonObject;
import io.vertx.core.logging.Logger;
import io.vertx.core.logging.LoggerFactory;
import io.vertx.ext.web.client.HttpResponse;
import io.vertx.ext.web.client.WebClient;
import io.vertx.ext.web.client.WebClientOptions;

/**
 * @author <a href="mailto:julien@julienviet.com">Julien Viet</a>
 */
@SuppressWarnings("unused")
public class WebClientRequest implements Request {

  private static final Logger logger = LoggerFactory.getLogger(WebClientRequest.class);

  private final WebClient client;
  private final WebClientRequestBase request;
  private final SockJSMessageHandler handler;
  private final String uri;
  private final String scheme;
  private final String host;
  private final int port;
  private final String path;
  private final Map<String
