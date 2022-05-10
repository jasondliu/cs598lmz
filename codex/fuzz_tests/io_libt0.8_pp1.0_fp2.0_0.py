import io.swagger.annotations.ApiModelProperty;

/**
 * Created by wangyunfei on 2017/6/12.
 */
public class GetCategoryResponse {

    @ApiModelProperty("分类ID")
    private Long id;


    @ApiModelProperty("分类名称")
    private String name;

    @ApiModelProperty("是否是叶子节点，1是，0否")
    private Integer isLeaf;

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Integer getIsLeaf() {
        return isLeaf;
    }

    public void setIsLeaf(Integer isLeaf) {
        this.isLeaf = isLeaf;
    }
