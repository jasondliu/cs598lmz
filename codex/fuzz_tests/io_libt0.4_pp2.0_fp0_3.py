import io.vertx.core.http.HttpServerResponse;
import io.vertx.core.json.Json;
import io.vertx.core.json.JsonArray;
import io.vertx.core.json.JsonObject;
import io.vertx.ext.jdbc.JDBCClient;
import io.vertx.ext.sql.SQLConnection;
import io.vertx.ext.web.Router;
import io.vertx.ext.web.RoutingContext;
import io.vertx.ext.web.handler.BodyHandler;
import io.vertx.ext.web.handler.StaticHandler;

public class RestVerticle extends AbstractVerticle {
	
	private JDBCClient jdbc;
	
	@Override
	public void start(Future<Void> future) throws Exception {
		
		jdbc = JDBCClient.createShared(vertx, new JsonObject()
				.put("url", "jdbc:mysql://localhost:3306/test")
				.put("driver_
