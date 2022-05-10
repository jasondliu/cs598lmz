import io.micronaut.function.client.FunctionClient;
import io.micronaut.http.annotation.Body;
import javax.inject.Named;
import java.util.List;
import javax.validation.constraints.NotBlank;
import raf.functions.Data;

@FunctionClient
public interface LearnData {

    @Named("learn-data")
    Data apply(@Body @NotBlank List<String> list) ;

}
