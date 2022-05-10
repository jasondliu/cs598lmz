import io.netty.handler.codec.http.HttpResponseStatus;
import io.netty.handler.codec.http.HttpVersion;

public class HttpResponse {

	private HttpVersion version;
	private HttpResponseStatus status;
	private HttpHeaders headers;
	private ByteBuf content;

	public HttpResponse(HttpVersion version, HttpResponseStatus status, HttpHeaders headers, ByteBuf content) {
		this.version = version;
		this.status = status;
		this.headers = headers;
		this.content = content;
	}

	public HttpVersion getVersion() {
		return version;
	}

	public HttpResponseStatus getStatus() {
		return status;
	}

	public HttpHeaders getHeaders() {
		return headers;
	}

	public ByteBuf getContent() {
		return content;
	}

}
