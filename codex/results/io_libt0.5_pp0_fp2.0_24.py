import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import lombok.Data;

import java.io.Serializable;
import java.util.Date;

/**
 * @author: wangsaichao
 * @date: 2018/5/4
 * @description: 用户角色关联表
 */
@Data
@ApiModel
public class SysUserRole implements Serializable {

    private static final long serialVersionUID = 1L;

    /**
     * 主键id
     */
    @ApiModelProperty(value = "主键id")
    private Integer id;
    /**
     * 用户id
     */
    @ApiModelProperty(value = "用户id")
    private Integer userId;
    /**
     * 角色id
     */
    @ApiModelProperty(value = "角色id")
    private Integer roleId;
   
