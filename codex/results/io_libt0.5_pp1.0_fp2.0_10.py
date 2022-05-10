import io.netty.handler.codec.http.HttpResponseStatus;
import io.netty.util.CharsetUtil;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.util.concurrent.atomic.AtomicBoolean;

/**
 * @author <a href="mailto:julien@julienviet.com">Julien Viet</a>
 */
public class HttpClientRequestImpl extends HttpClientRequest {

  private final Logger log = LoggerFactory.getLogger(HttpClientRequestImpl.class);
  private final HttpClientImpl client;
  private final HttpRequest request;
  private final Handler<HttpVersion> writeHead;
  private final Handler<Buffer> dataHandler;
  private final Handler<Void> endHandler;
  private final Handler<Throwable> exceptionHandler;
  private final AtomicBoolean headWritten = new AtomicBoolean();
  private final AtomicBoolean ended = new AtomicBoolean();
  private final AtomicBoolean reset = new AtomicBoolean();
  private
