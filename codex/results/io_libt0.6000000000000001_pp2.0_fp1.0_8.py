import io.swagger.annotations.ApiModelProperty;

import java.io.Serializable;
import java.util.Date;

/**
 * @author: zc
 * @description: 车辆信息
 * @time: 2020/4/20 0020 上午 9:12
 */
@ApiModel
public class CarInfo implements Serializable {

    @ApiModelProperty(value = "车牌号")
    private String carNo;

    @ApiModelProperty(value = "车架号")
    private String carVin;

    @ApiModelProperty(value = "车辆颜色")
    private String carColor;

    @ApiModelProperty(value = "车辆品牌")
    private String carBrand;

    @ApiModelProperty(value = "车辆所属人")
    private String owner;

    @ApiModelProperty(value = "车辆
