import io.swagger.annotations.ApiModelProperty;
import lombok.Data;

import java.util.List;

@Data
@ApiModel(value = "视频类别列表")
public class VideoTypeListDTO {

    @ApiModelProperty(value = "视频类型集合")
    private List<VideoTypeDTO> videoTypeDTOS;
}
