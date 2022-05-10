import io.vertx.core.Vertx;
import io.vertx.core.json.JsonObject;
import io.vertx.ext.unit.Async;
import io.vertx.ext.unit.TestContext;
import io.vertx.ext.unit.junit.VertxUnitRunner;
import net.roboconf.core.utils.Utils;

/**
 * @author Vincent Zurczak - Linagora
 */
@RunWith(VertxUnitRunner.class)
public class LoggerFactoryTest {

	@Test
	public void testCreationWithNoParameters( TestContext context ) throws Exception {
		Vertx vertx = Vertx.vertx();
		Utils.doQuietly( () -> vertx.close());
		vertx.deployVerticle( LoggerFactory.class.getName(), context.asyncAssertSuccess());
	}

	@Test
	public void testLogAndSetLevel( TestContext context ) throws Exception {
		Vertx vertx = Vertx.vertx();
		Async async = context.async();
		
