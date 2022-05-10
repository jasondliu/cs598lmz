import io.netty.handler.codec.http.HttpResponseStatus;
import io.netty.handler.codec.http.HttpUtil;
import io.netty.handler.codec.http.HttpVersion;
import io.netty.util.concurrent.Future;
import io.netty.util.concurrent.GenericFutureListener;

/**
 * @author <a href="mailto:julien@julienviet.com">Julien Viet</a>
 */
public class HttpServerTest extends HttpTestBase {

  private HttpServer server;
  private HttpClient client;

  @Override
  protected void setUp() throws Exception {
    super.setUp();
    server = vertx.createHttpServer(new HttpServerOptions().setPort(HttpTestBase.DEFAULT_HTTP_PORT));
    client = vertx.createHttpClient(new HttpClientOptions());
  }

  @Override
  protected void tearDown() throws Exception {
    if (server != null) {
      CountDownLatch latch = new CountDownLatch(1);

