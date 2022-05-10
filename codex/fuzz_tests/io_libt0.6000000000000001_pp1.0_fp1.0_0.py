import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import java.io.IOException;
import org.threeten.bp.OffsetDateTime;

/**
 * Информация о текущем состоянии договора.
 */
@ApiModel(description = "Информация о текущем состоянии договора.")
@javax.annotation.Generated(value = "io.swagger.codegen.languages.JavaClientCodegen", date = "2020-03-24T08:13:36.359Z")
public class ContractStatusInfo {
  @SerializedName("status")
  private ContractStatusTypeEnum status = null;

  @SerializedName("statusDate")
  private OffsetDateTime statusDate = null;

  @
