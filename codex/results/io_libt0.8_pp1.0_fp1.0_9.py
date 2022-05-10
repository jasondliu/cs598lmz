import io.swagger.annotations.ApiModelProperty;

/**
 * CreateUserRequest
 */
@javax.annotation.Generated(value = "io.swagger.codegen.languages.JavaClientCodegen", date = "2020-01-15T01:09:57.384Z")
public class CreateUserRequest {
  @SerializedName("name")
  private String name = null;

  @SerializedName("email")
  private String email = null;

  @SerializedName("password")
  private String password = null;

  @SerializedName("phone")
  private String phone = null;

  @SerializedName("language")
  private String language = null;

  @SerializedName("role")
  private String role = null;

  @SerializedName("enabled")
  private Boolean enabled = null;

  @SerializedName("2fa")
  private Boolean _2fa = null;

  public CreateUserRequest name(String name) {
    this.name = name;
    return this;
  }

   /**
   * Get name
  
