import io.swagger.annotations.ApiModelProperty;
import lombok.Data;

/**
 * @author billchen
 * @version 1.0
 * @create 2020-12-12 10:40
 **/
@Data
public class LogQueryDto {

	@ApiModelProperty(value = "系统模块")
	private String serviceId;

	@ApiModelProperty(value = "操作类型")
	private String operation;

	@ApiModelProperty(value = "操作用户")
	private String username;

	@ApiModelProperty(value = "耗时")
	private String time;

	/**
	 * 开始时间
	 */
	@ApiModelProperty(value = "开始时间")
	private String createTimeFrom;

	/**
	 * 结束时间
	 */
	@ApiModelProperty(value = "结束时间")

