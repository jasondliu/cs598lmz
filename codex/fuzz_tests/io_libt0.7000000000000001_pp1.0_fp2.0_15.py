import io.swagger.annotations.ApiModelProperty;

/**
 * 问题分类管理参数
 *
 * @author linsm
 * @since 2020-06-17
 */
@ApiModel(value = "问题分类管理参数")
public class ProblemCatDTO extends BaseDTO {

    /**
     * 问题分类名称
     */
    @ApiModelProperty(value = "问题分类名称")
    @NotBlank(message = "问题分类名称不能为空")
    private String catName;

    /**
     * 问题分类描述
     */
    @ApiModelProperty(value = "问题分类描述")
    private String catDesc;


    public String
