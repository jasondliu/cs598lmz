import io.swagger.annotations.ApiModelProperty;
import lombok.Data;

import java.io.Serializable;
import java.util.Date;

/**
 * @author: zhangyh-k
 * @date: 2018/10/23
 * @description:
 */
@Data
@ApiModel(value = "组织机构")
public class SysOrganization implements Serializable {
    private static final long serialVersionUID = -8589698204017834593L;
    @ApiModelProperty(value = "主键id")
    private Long id;
    @ApiModelProperty(value = "父id")
    private Long pid;
    @ApiModelProperty(value = "组织机构名称")
    private String name;
    @ApiModelProperty(value = "组织机构编码")
    private String code;
    @ApiModelProperty(value = "组
