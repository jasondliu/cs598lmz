import io.swagger.annotations.Api;
import io.swagger.annotations.ApiOperation;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.MediaType;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

/**
 * @author sophea <a href='mailto:sophea@redhat.com'> sophea </a>
 * @version $Revision$ $Date$
 */
@Api(value = "Account service")
@RestController
@RequestMapping("/v1/accounts")
@CrossOrigin(origins = "*")
public class AccountController {

    @Autowired

