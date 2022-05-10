import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;

import javax.validation.constraints.NotNull;
import java.io.Serializable;
import java.util.Objects;

/**
 * A DTO for the {@link com.kode.ts.domain.EstatusAcademico} entity.
 */
@ApiModel(description = "Estatus Academico")
public class EstatusAcademicoDTO implements Serializable {

    private Long id;

    /**
     * Estatus Academico
     */
    @NotNull
    @Size(min = 1, max = 50)
    @ApiModelProperty(value = "Estatus Academico", required = true)
    private String estatus;

    // jhipster-needle-entity-add-field - JHipster will add fields here, do not remove


    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }
