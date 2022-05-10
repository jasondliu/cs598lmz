import io.vertx.core.json.JsonObject;
import io.vertx.ext.sql.SQLConnection;
import io.vertx.ext.web.RoutingContext;
import io.vertx.ext.web.templ.TemplateEngine;

public class AddNewStudentController extends AbstractController {
	private final TemplateEngine engine;

	public AddNewStudentController(TemplateEngine engine) {
		this.engine = engine;
	}

	@Override
	public void get(RoutingContext context, SQLConnection connection) {
		JsonObject data = new JsonObject();
		data.put("title", "Add New Student");
		engine.render(data, "templates/addNewStudent.ftl", res -> {
			if (res.succeeded()) {
				context.response().putHeader("Content-Type", "text/html");
				context.response().end(res.result());
			} else {
				context.fail(res.cause());
			}
		});
	}
