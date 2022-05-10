import io.swagger.annotations.ApiModelProperty;

/**
 * FrontendController
 * 注释:前端控制器
 * @author zhou.xy
 * @date 2019/8/8
 */
@ApiModel(value = "FrontendController",description = "前端控制器")
public class FrontendController {
    @ApiModelProperty(value = "区域编码")
    private String areaCode;
    @ApiModelProperty(value = "规划类型 普通(1)、精品(2)")
    private String planNo;
    @ApiModelProperty(value = "控制器状态 空闲(1)、忙碌(2)")
    private String controllerStatus;
    @ApiModelProperty(value = "维护区域")
    private String maintenanceArea;
    @A
