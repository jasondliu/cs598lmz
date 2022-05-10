import io.swagger.annotations.ApiModelProperty;
import lombok.Data;

import java.io.Serializable;
import java.util.Date;

/**
 * @author: hxy
 * @description: 定时任务日志
 * @date: 2017/10/24 11:14
 */
@Data
@ApiModel(value = "定时任务日志")
public class ScheduleJobLogEntity implements Serializable {
	private static final long serialVersionUID = 1L;
	
	/**
	 * 日志id
	 */
	@ApiModelProperty(value = "日志id", required = true)
	private Long logId;
	
	/**
	 * 任务id
	 */
	@ApiModelProperty(value = "任务id", required = true)
	private Long jobId;
	
	/**
	 * spring bean名称
	 */
	@ApiModelProperty(value = "spring bean名
