import io.swagger.annotations.ApiModelProperty;
import lombok.Data;

import javax.validation.constraints.NotBlank;

/**
 * @author: liuqiang
 * @create: 2020-06-16 15:43
 *
 * 创建课程信息的封装对象
 */
@Data
public class CourseInfoVO {

    @ApiModelProperty(value = "课程名称")
    @NotBlank(message = "课程名称不能为空")
    private String title;

    @ApiModelProperty(value = "课程销售价格，设置为0则可免费观看")
    private String price;

    @ApiModelProperty(value = "总课时")
    private Integer lessonNum;

    @ApiModelProperty(value =
