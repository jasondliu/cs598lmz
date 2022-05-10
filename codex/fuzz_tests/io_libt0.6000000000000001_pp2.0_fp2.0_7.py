import io.netty.handler.codec.http.HttpResponseStatus;
import io.netty.handler.codec.http.HttpVersion;

public class HttpResponse {
	private HttpResponseStatus status = HttpResponseStatus.OK;
	private HttpVersion version = HttpVersion.HTTP_1_1;
	private HttpHeaders headers = new DefaultHttpHeaders();
	private byte[] content;
	
	public HttpResponseStatus getStatus() {
		return status;
	}
	public void setStatus(HttpResponseStatus status) {
		this.status = status;
	}
	public HttpVersion getVersion() {
		return version;
	}
	public void setVersion(HttpVersion version) {
		this.version = version;
	}
	public HttpHeaders getHeaders() {
		return headers;
	}
	public void setHeaders(HttpHeaders headers) {
		this.headers = headers;
	}
	public byte[] getContent() {
		return content;
	}
	public void
