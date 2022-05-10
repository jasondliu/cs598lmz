import io.sunshower.common.Identifier;
import java.util.ArrayList;
import java.util.Collection;
import java.util.List;
import java.util.Objects;
import java.util.Optional;
import java.util.Set;
import java.util.stream.Collectors;
import javax.inject.Inject;
import lombok.val;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

@Controller
@RequestMapping("/api/core/properties")
@ResponseBody
@AllArgsConstructor
public class PropertyElementController {

  private final PropertyElementService propertyElementService;

  private final PropertyElementRepository<PropertyElement, Identifier>
      propertyElementRepository;

  @Inject private PropertyElementConverter converter;

  @GetMapping("{id}")
  public PropertyElement get(
      @PathVariable("id") PropertyElement.Scope scope, @PathVariable("id") Identifier id) {
    val property =
        Optional.ofNullable(
