import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import lombok.Data;

@Data
@ApiModel(value = "车辆类型列表返回值")
public class CarTypeListResp {

    @ApiModelProperty(name = "carTypeId", value = "车辆类型ID", required = true)
    private Long carTypeId;

    @ApiModelProperty(name = "carTypeName", value = "车辆类型名称", required = true)
    private String carTypeName;

    @ApiModelProperty(name = "carTypeStatus", value = "车辆类型状态", required = true)
    private String carTypeStatus;

    @ApiModelProperty(name = "carTypeStatusDesc", value = "车辆类型状态
