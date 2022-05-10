import io.pivotal.cfapp.service.ApplicationInfoService;
import io.pivotal.cfapp.service.CredentialCache;
import io.pivotal.cfapp.service.DashboardExceptionService;

@Component
public class Recycler {

    private static final Logger logger = LoggerFactory.getLogger(Recycler.class);
    private static final String API_URI = "/v3/apps/%s";
    private final ApplicationInfoService starService;
    private final DashboardExceptionService excService;
    private final CredentialCache cache;
    private final CredentialsProvider credentialsProvider;
    private final DashboardProperties props;

    @Autowired
    public Recycler(
            ApplicationInfoService starService,
            DashboardExceptionService excService,
            CredentialCache cache,
            CredentialsProvider credentialsProvider,
            DashboardProperties props) {
        this.starService = starService;
        this.excService = excService;
        this.cache = cache;
        this.credentialsProvider = credentialsProvider;
        this.
