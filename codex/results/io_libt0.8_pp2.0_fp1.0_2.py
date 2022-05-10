import io.netty.handler.codec.http.FullHttpResponse;

/**
 * HTTP响应数据接口
 * 
 * @author 	yinhaiquan
 * @date	2018-06-04 17:06:37
 */
public interface IHttpResponseData {
	/**
	 * 获取HTTP响应自身的数据
	 * 
	 * @return
	 */
	FullHttpResponse getHttpResponseData();
	
	/**
	 * 设置HTTP响应自身的数据
	 * 
	 * @param response
	 */
	void setHttpResponseData(FullHttpResponse response);
	
	/**
	 * 设置HTTP状态码
	 * 
	 * @param httpCode
	 */
	void setHttpCode(int httpCode);
	
	/**
	 * 获取HTTP状态码

