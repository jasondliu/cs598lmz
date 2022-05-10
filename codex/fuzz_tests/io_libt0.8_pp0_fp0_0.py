import io.vertx.core.json.JsonObject;
import io.vertx.ext.web.RoutingContext;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

import java.util.function.Consumer;

/**
 * Created by alberto on 2016-11-24.
 */
public class HealthCheckHandler implements Consumer<RoutingContext> {
    private static final Logger logger = LogManager.getLogger(HealthCheckHandler.class);

    @Override
    public void accept(final RoutingContext routingContext) {
        final JsonObject object = new JsonObject();
        object.put("status", "ok");
        routingContext.response().end(object.encode());
    }
}
