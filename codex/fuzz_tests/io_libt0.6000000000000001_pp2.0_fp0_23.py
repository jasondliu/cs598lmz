import io.swagger.annotations.ApiModelProperty;

/**
 * 请求报文
 * @author sun
 *
 */
public class ReqModel<T> {

	@ApiModelProperty(value = "请求参数")
	private T params;

	@ApiModelProperty(value = "应用密钥")
	private String appkey;

	@ApiModelProperty(value = "时间戳")
	private String timestamp;

	@ApiModelProperty(value = "签名")
	private String sign;

	public T getParams() {
		return params;
	}

	public void setParams(T params) {
		this.params = params;
	}

	public String getAppkey() {
		return appkey;
	}

	public void setAppkey(String appkey) {
		this.appkey = appkey;
	}

	public String getTimestamp() {
		return timestamp;
	}
