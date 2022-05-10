import io.swagger.annotations.ApiModelProperty;
import lombok.Data;

import java.io.Serializable;
import java.util.Date;

/**
 * @author: zhangyh-k
 * @date: 2018/10/22
 * @description:
 */
@Data
public class SysUser implements Serializable {

    private static final long serialVersionUID = -5886012896705137070L;
    /**
     *
     */
    private Integer id;
    /**
     * 用户名
     */
    private String username;
    /**
     * 密码
     */
    private String password;
    /**
     * 部门ID
     */
    private Integer deptId;
    /**
     * 邮箱
     */
    private String email;
    /**
     * 联系电话
     */
    private String mobile;
    /**
     * 状态 0锁定 1有效
    
