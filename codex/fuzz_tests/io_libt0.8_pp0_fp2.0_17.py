import io.vertx.core.Handler;
import io.vertx.core.json.JsonObject;
import io.vertx.ext.jdbc.JDBCClient;
import io.vertx.ext.sql.ResultSet;
import io.vertx.ext.sql.SQLConnection;
import io.vertx.ext.web.RoutingContext;

/**
 * Created by gtam on 3/10/16.
 */
public class InsertUser implements Handler<RoutingContext> {
    @Override
    public void handle(RoutingContext routingContext) {
        JsonObject jsonObject = routingContext.getBodyAsJson();
        String name = jsonObject.getString("name");
        String age = jsonObject.getString("age");
        String sex = jsonObject.getString("sex");

        JsonObject result = new JsonObject();

        JDBCClient jdbcClient = vertx.JDBCClient.createShared(vertx, new JsonObject().put("url", "jdbc:h2:~/test"));
        jdbcClient.getConnection
