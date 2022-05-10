import io.swagger.annotations.Api;
import io.swagger.annotations.ApiOperation;

@RestController
@RequestMapping("/v1/orden")
@Api(value = "Orden Service", description = "Service for orden")
public class OrdenController {

    private static final Logger LOG = LoggerFactory.getLogger(OrdenController.class);

    @Autowired
    private OrdenService ordenService;

    @Autowired
    private OrdenValidator ordenValidator;

    @Autowired
    private CatalogoValidator catalogoValidator;

    @Autowired
    private ItemValidator itemValidator;

    @Autowired
    private ItemService itemService;

    @Autowired
    private CatalogoService catalogoService;

    @GetMapping("")
    @ApiOperation(value = "Get All ordens", response = Orden.class, responseContainer = "List")
    public ResponseEntity<?> findAllOrdens() {
        LOG.info("Find all ordens");
        try {

