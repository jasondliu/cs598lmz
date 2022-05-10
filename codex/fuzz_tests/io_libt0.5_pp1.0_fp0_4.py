import io.swagger.annotations.ApiModelProperty;

/**
 * @author zhongqiang.qiu
 * @version V1.0
 * @Package com.qiu.common.entity
 * @Description: 抽象实体基类
 * @date 2016/11/2 20:57
 */
public abstract class AbstractEntity<ID extends Serializable> extends AbstractPersistable<ID> implements Persistable<ID> {

    /**
     * 是否有效
     */
    @ApiModelProperty(value = "是否有效")
    protected Boolean valid;

    /**
     * 创建人
     */
    @ApiModelProperty(value = "创建人")
    protected String createUser;

    /**
     * 创建时间
     */
    @ApiModelProperty(value = "创建时间")
    protected Date createTime;

    /**
     * 更新人
    
