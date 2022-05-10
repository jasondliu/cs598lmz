import io.vertx.core.json.JsonObject;
import io.vertx.ext.unit.Async;
import io.vertx.ext.unit.TestContext;
import io.vertx.ext.unit.junit.RunTestOnContext;
import io.vertx.ext.unit.junit.VertxUnitRunner;
import org.junit.Rule;
import org.junit.Test;
import org.junit.runner.RunWith;

import java.util.Arrays;
import java.util.List;

@RunWith(VertxUnitRunner.class)
public class TestVertxClient {

    @Rule
    public RunTestOnContext rule = new RunTestOnContext();

    @Test
    public void testGet(TestContext context) {
        Async async = context.async();
        VertxClient client = new VertxClient(rule.vertx());
        client.get("http://localhost:8080/api/v1/books", response -> {
            context.assertEquals(200, response.statusCode());
            response.bodyHandler(body
