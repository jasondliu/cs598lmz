import io.swagger.annotations.ApiResponse;
import lombok.RequiredArgsConstructor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import javax.validation.Valid;
import java.util.List;

@RestController
@RequestMapping(Endpoint.PERSONS_ENDPOINT)
@RequiredArgsConstructor
@Api(tags = AppConstants.PERSON_TAG)
public class PersonController {

    @Autowired
    private final PersonService personService;

    @GetMapping
    @ApiOperation(value = "Get all persons", response = List.class)
    @ApiResponse(code = 200, message = "Successfully retrieved list")
    public ResponseEntity<List<PersonDto>> getAllPersons(){
        return new ResponseEntity<>(personService.getAll(), HttpStatus.OK);
    }

    @Get
