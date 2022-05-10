import io.swagger.annotations.ApiModelProperty;

import java.io.Serializable;
import java.util.Date;

public class Comment implements Serializable {

    /**
     * 主键
     */
    @ApiModelProperty(value = "主键")
    private Long id;

    /**
     * 评论用户id
     */
    @ApiModelProperty(value = "评论用户id")
    private Long userId;

    /**
     * 评论内容
     */
    @ApiModelProperty(value = "评论内容")
    private String content;

    /**
     * 评论创建时间
     */
    @ApiModelProperty(value = "评论创建时间")
    private Date createdTime;

    /**
     * 评论更新时间
     */
   
