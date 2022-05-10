import io.vertx.core.Future;

/**
 * start the verticle in the context of the Vert.x instance.
 * 
 * @author jimmy
 *
 */
public class Example1 {
	public static void deployVerticle(Vertx vertx, String name) {
		vertx.deployVerticle(name);
	}
	
	public static void main(String [] args) {
	    Vertx vertx = Vertx.vertx();
	    String name = HelloWorldVerticle.class.getName();
	    deployVerticle(vertx, name);
	}
}
