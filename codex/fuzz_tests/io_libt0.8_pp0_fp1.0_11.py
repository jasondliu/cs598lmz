import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;

import java.io.Serializable;

@ApiModel(value = "表格表头设置")
public class TableHeader implements Serializable {
    @ApiModelProperty(value = "表头名称")
    private String name;
    @ApiModelProperty(value = "表头对应字段名称")
    private String dataIndex;
    @ApiModelProperty(value = "是否显示")
    private boolean isShow;
    @ApiModelProperty(value = "表头排序")
    private int sort;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getDataIndex() {
        return dataIndex;
    }

    public void setDataIndex(String dataIndex
