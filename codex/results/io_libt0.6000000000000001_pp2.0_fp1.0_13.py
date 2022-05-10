import io.swagger.annotations.ApiModelProperty;
import org.hibernate.validator.constraints.NotBlank;

import javax.validation.constraints.NotNull;

public class ActivateUserRequest {

    @ApiModelProperty(value = "Идентификатор пользователя", required = true, dataType = "String")
    @NotNull(message = "Идентификатор пользователя отсутствует")
    @NotBlank(message = "Идентификатор пользователя отсутствует")
    private String id;

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
