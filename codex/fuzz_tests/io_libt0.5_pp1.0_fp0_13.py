import io.vertx.core.json.JsonObject;

/**
 * @author <a href="mailto:julien@julienviet.com">Julien Viet</a>
 */
public class VertxServiceLoader implements ServiceLoader {

  private final Vertx vertx;

  public VertxServiceLoader(Vertx vertx) {
    this.vertx = vertx;
  }

  @Override
  public <T> void load(Class<T> service, Handler<AsyncResult<T>> resultHandler) {
    vertx.executeBlocking(f -> {
      ServiceLoader<T> loader = ServiceLoader.load(service, VertxServiceLoader.class.getClassLoader());
      f.complete(loader);
    }, ar -> {
      if (ar.failed()) {
        resultHandler.handle(Future.failedFuture(ar.cause()));
      } else {
        ServiceLoader<T> loader = (ServiceLoader<T>) ar.result();
        Iterator<T> iter = loader.iterator();
        if (iter.hasNext()) {
          resultHandler.handle
