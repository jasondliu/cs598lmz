import io.vertx.core.json.JsonObject;
import io.vertx.core.logging.Logger;
import io.vertx.core.logging.LoggerFactory;

public class PluginService extends BaseService {

	private static Logger log = LoggerFactory.getLogger(PluginService.class);
	private static final String PLUGIN_COLLECTION = "plugins";

	private static final Map<String, Plugin> plugins = new HashMap<>();

	private static final PluginService INSTANCE = new PluginService();

	private PluginService() {

	}

	public static PluginService getInstance() {
		return INSTANCE;
	}

	public void init(Vertx vertx) {
		super.init(vertx);
		initPlugins();
	}

	private void initPlugins() {

		try {
			MongoClient mongo = MongoClient.createShared(vertx, new JsonObject(), "LMS_PLUGIN");
			mongo.find(PLUGIN_COLLECTION, new JsonObject(),
