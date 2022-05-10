import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import org.springframework.format.annotation.DateTimeFormat;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import java.util.Date;

@Entity
@ApiModel(value = "日志",description = "日志")
public class LogBean {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private int id;//id
    @ApiModelProperty(value = "用户id",required = true)
    private int userId;//用户id
    @ApiModelProperty(value = "时间",required = true)
    @DateTimeFormat(pattern = "yyyy-MM-dd HH:mm:ss")
    private Date date;//时间
    @ApiModelProperty(
