import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import java.io.Serializable;
import java.util.Date;
import lombok.Data;

/**
 * 商品评价回复关系
 * 
 * @author liqingbi
 * @email 1130274947@qq.com
 * @date 2020-08-09 13:35:33
 */
@ApiModel
@Data
@TableName("pms_comment_replay")
public class CommentReplayEntity implements Serializable {
	private static final long serialVersionUID = 1L;

	/**
	 * $column.comments
	 */
	@TableId
	@ApiModelProperty(name = "id",value = "$column.comments")
	private Long id;
	/**
	 * $column.comments
	 */
	@ApiModelProperty(name = "commentId",value = "$column.comments")
	private Long commentId;
	/**
	 * $column.comments
