import io.vertx.core.eventbus.Message;
import io.vertx.core.http.HttpMethod;
import io.vertx.core.json.JsonObject;

public class UserRouter extends AbstractRouter {

  public UserRouter(Vertx vertx, Router router) {
    super(vertx, router);
  }

  @Override
  public void setRouting() {
    router.route(HttpMethod.GET, "/users").handler(this::getUserList);
    router.route(HttpMethod.POST, "/users").handler(this::createUser);
    router.route(HttpMethod.GET, "/users/:userId").handler(this::getUser);
    router.route(HttpMethod.PATCH, "/users/:userId").handler(this::updateUser);
    router.route(HttpMethod.DELETE, "/users/:userId").handler(this::deleteUser);
  }

  private void createUser(RoutingContext ctx) {
    JsonObject user = ctx.getBodyAsJson();
    vertx.eventBus().
