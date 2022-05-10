import io.netty.handler.codec.http.HttpHeaderNames;
import io.netty.handler.codec.http.HttpHeaders;
import io.netty.handler.codec.http.HttpResponse;
import io.netty.handler.codec.http.HttpUtil;
import io.netty.util.AsciiString;

import java.nio.charset.CharsetDecoder;
import java.util.List;

/**
 * @author <a href="mailto:ales.justin@jboss.org">Ales Justin</a>
 */
public class NettyHttpResponse extends AbstractHttpResponse<FullHttpResponse> {
    private final CharsetDecoder decoder;
    private final HttpHeaders headers;

    public NettyHttpResponse(FullHttpResponse response, Object entity, CharsetDecoder decoder) {
        super(response, entity);
        this.decoder = decoder;
        this.headers = response.headers();
    }

    @Override
    protected void setEntity(Object entity) {
        response.content
