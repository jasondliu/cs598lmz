import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import org.hibernate.validator.constraints.NotBlank;

import javax.persistence.*;
import java.util.List;

/**
 * Created by l.li on 2016/4/22.
 */
@ApiModel(value = "话题")
@Entity
@Table(name = "topic")
public class Topic extends BaseModel {

    @ApiModelProperty(value = "话题名称")
    @NotBlank(message = "话题名称不能为空")
    @Column(name = "name")
    private String name;

    @ApiModelProperty(value = "话题描述")
    @Column(name = "description")
    private String description;

    @ApiModelProperty(value = "话题图片")
    @Column(name = "image")
