import io.vertx.ext.web.Router;

public class WebRoute implements Route {
    @Override
    public void registerRoute(Router router) {
        router.route("/").handler(ctx -> ctx.response().end("Hello from vertx"));
        router.route("/users").handler(ctx -> {
            ctx.response().end("List of users");
        });
        router.route("/users/:id").handler(ctx -> {
            String userId = ctx.request().getParam("id");
            ctx.response().end("Info of the user " + userId);
        });
    }
}
