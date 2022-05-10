import io.swagger.annotations.ApiModelProperty;

import java.io.Serializable;
import java.util.Date;

/**
 * Created by pengl on 2018/5/30.
 */
public class DeliveryBillView implements Serializable {

    private static final long serialVersionUID = -6258672626082346177L;

    @ApiModelProperty("物流单号")
    private String billNumber;

    @ApiModelProperty("物流公司")
    private String logisticsCompany;

    @ApiModelProperty("发货日期")
    private Date deliveryTime;

    @ApiModelProperty("送货地址")
    private String deliveryAddress;

    @ApiModelProperty("收货人")
    private String receiver;

    @ApiModelProperty("联系电话")
    private String receiverPhone;

    @ApiModelProperty("备注")
    private String remark;

    public String getBillNumber()
