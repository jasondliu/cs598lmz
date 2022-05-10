import io.mosip.registration.processor.manual.verification.dto.DecisionInfoDto;
import io.swagger.annotations.ApiModelProperty;

/**
 * The Class ManualVerificationDTO.
 */
public class ManualVerificationDTO {
	
	/** The id. */
	@ApiModelProperty(value = "id", position = 1)
	@NotNull
	private String id;
	
	/** The version. */
	@ApiModelProperty(value = "version", position = 2)
	@NotNull
	private String version;
	
	/** The decision. */
	@ApiModelProperty(value = "decision", position = 3)
	@NotNull
	private String decision;
	
	/** The comments. */
	@ApiModelProperty(value = "comments", position = 4)
	private String comments = "";
	
	/** The created by. */
	@ApiModelProperty(value = "createdBy", position = 5)
	private String createdBy = "MOSIP";
	
	/** The
