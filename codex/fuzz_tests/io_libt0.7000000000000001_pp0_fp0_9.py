import io.swagger.annotations.ApiModelProperty;
import lombok.Data;

import java.io.Serializable;
import java.util.Date;

/**
 * @author: zhangzl
 * @description:
 * @date: 2018/1/3 16:18
 */
@Data
@ApiModel(description = "接口统计数据")
public class ApiStatistic implements Serializable {

    private static final long serialVersionUID = -3466373614782027031L;

    @ApiModelProperty(value = "访问者id")
    private Integer id;

    @ApiModelProperty(value = "访问者名称")
    private String name;

    @ApiModelProperty(value = "访问者ip")
    private String ip;

    @ApiModelProperty(value = "访问者mac")
    private String mac;

    @ApiModelProperty(value = "访问地
