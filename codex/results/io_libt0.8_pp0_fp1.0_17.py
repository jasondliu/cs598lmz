import io.vertx.core.http.HttpServerRequest;
import io.vertx.core.http.HttpServerResponse;
import io.vertx.core.json.Json;
import io.vertx.core.json.JsonArray;
import io.vertx.core.json.JsonObject;
import io.vertx.ext.web.RoutingContext;

import java.util.List;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.logging.Logger;

/**
 * Created by sgarlick on 2/5/15.
 */
public class CategoryController {
    private final static Logger LOG  = Logger.getLogger(CategoryController.class.getName());

    private Service<String, List<Product>> service;
    private String jsonHeader = "application/json";

    public CategoryController(Service<String, List<Product>> service) {
        this.service = service;
    }

    public void getAllProductsForCategory(RoutingContext routingCtx) {

        HttpServerResponse response = routingCtx
