import io.vertx.core.json.JsonObject;
import io.vertx.ext.unit.Async;
import io.vertx.ext.unit.TestContext;
import io.vertx.ext.unit.junit.VertxUnitRunner;
import io.vertx.ext.web.client.WebClient;
import io.vertx.ext.web.client.WebClientOptions;
import org.junit.Before;
import org.junit.Test;
import org.junit.runner.RunWith;

import java.util.HashMap;
import java.util.Map;

import static com.github.tomakehurst.wiremock.client.WireMock.*;
import static org.junit.Assert.assertEquals;

@RunWith(VertxUnitRunner.class)
public class ApiVerticleTest {

    private static final String LOCALHOST = "localhost";
    private static final String WIREMOCK_HOST = "http://localhost:8089";
    private static final String WIREMOCK_API_ENDPOINT = "/api";

