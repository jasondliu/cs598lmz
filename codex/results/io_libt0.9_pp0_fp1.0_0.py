import io.vertx.ext.web.Router;
import io.vertx.ext.web.RoutingContext;
import io.vertx.ext.web.handler.BodyHandler;

public class ApiVerticle extends AbstractVerticle {
    @Override
    public void start() throws Exception {
        Router router = Router.router(vertx);
        router.route().handler(BodyHandler.create());

        ((Router) ((Router) router.route("/test").handler(context -> {
            context.next();
        }).failureHandler(context -> {
            System.out.println(context.failure());
        })).route("/f").handler(context -> {
            context.response().setStatusMessage(context.response().statusMessage()).end();
        })).route("/z").handler(context -> {
            context.response().setStatusCode(200).end();
        });
        router.route("/test/*").handler(context -> {
            context.response().end();
        });

        router.route("/test/:id").handler(context -> {

