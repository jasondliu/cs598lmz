import io.gridgo.utils.pojo.PojoGetter;
import lombok.AccessLevel;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@AllArgsConstructor
@NoArgsConstructor
@Getter
public class FieldInjectorDefinition implements InjectorDefinition {

    private static final long serialVersionUID = -2734961012831957308L;

    private transient Field field;

    @SerializedName("fieldName")
    private String fieldName;

    @SerializedName("targetClass")
    private Class<?> targetClass;

    @SerializedName("fieldClass")
    private Class<?> fieldClass;

    @SerializedName("supportNull")
    private boolean supportNull;

    @Setter(AccessLevel.NONE)
    @Transient
    private PojoGetter getter;

    @Setter(AccessLevel.NONE)
    @Transient
    private PojoSetter setter;

    private void init() {
