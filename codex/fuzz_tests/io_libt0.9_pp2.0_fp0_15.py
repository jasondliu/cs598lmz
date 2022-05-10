import io.vertx.core.eventbus.Message;
import io.vertx.core.http.HttpServerResponse;
import io.vertx.core.json.Json;
import io.vertx.core.json.JsonArray;
import io.vertx.core.json.JsonObject;
import io.vertx.ext.web.RoutingContext;
import io.vertx.ext.web.templ.TemplateEngine;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import java.util.List;

/**
 * Created by zhouchuang on 2017/5/5.
 */
public class ArticleHandler  extends BaseHandler  {
    private static final Logger logger = LoggerFactory.getLogger(ArticleHandler.class);
    private TemplateEngine engine;
    private JsonObject config;
    private final String header = "X-Total-Count";
    public ArticleHandler(Vertx vertx){
        super(vertx);
    }

    @Override
    public void init(TemplateEngine engine, Json
