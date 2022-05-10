import io.vertx.core.json.JsonObject;
import io.vertx.ext.web.RoutingContext;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.util.Optional;

/**
 * Created by sudhiry on 2/20/18.
 */
public class UserHandler {

    private static final Logger LOGGER = LoggerFactory.getLogger(UserHandler.class);

    private final UserService userService;

    public UserHandler(UserService userService, Vertx vertx) {
        this.userService = userService;
    }

    public void getUser(RoutingContext routingContext) {
        String userId = routingContext.request().getParam("userId");
        if (userId == null) {
            routingContext.response().setStatusCode(400).end();
        } else {
            userService.getUser(userId).setHandler(res -> {
                if (res.succeeded()) {
                    routingContext.response()
                            .setStatusCode(200)
