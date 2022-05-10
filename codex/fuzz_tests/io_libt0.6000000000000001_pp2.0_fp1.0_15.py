import io.netty.handler.codec.http.HttpVersion;
import io.netty.util.CharsetUtil;
import java.util.List;
import java.util.Map;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

/**
 * @author jiang
 * @date 2019-08-25
 */
public class HttpClientInboundHandler extends SimpleChannelInboundHandler<HttpObject> {

  private static final Logger logger = LoggerFactory.getLogger(HttpClientInboundHandler.class);

  private boolean readingChunks;
  private final StringBuilder responseContent = new StringBuilder();

  private HttpResponse response;

  @Override
  public void channelRead0(ChannelHandlerContext ctx, HttpObject msg) throws Exception {
    if (msg instanceof HttpResponse) {
      HttpResponse response = this.response = (HttpResponse) msg;

      logger.info("STATUS: " + response.getStatus());
      logger.info("VERSION: " + response.getProtocolVersion());

      if
