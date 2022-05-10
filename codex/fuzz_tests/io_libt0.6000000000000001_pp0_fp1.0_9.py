import io.swagger.annotations.ApiModelProperty;
import lombok.Data;

import java.util.Date;

/**
 * @author 
 */
@Data
@ApiModel(value="会员表")
public class Member {
    @ApiModelProperty(value="id")
    private Long id;

    /**
     * 会员等级id
     */
    @ApiModelProperty(value="会员等级id")
    private Long levelId;

    /**
     * 用户名
     */
    @ApiModelProperty(value="用户名")
    private String username;

    /**
     * 密码
     */
    @ApiModelProperty(value="密码")
    private String password;

    /**
     * 昵称
     */
    @ApiModelProperty(value="昵称")
    private String nickname;

    /**
     * 手机
