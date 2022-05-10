import io.getstream.core.options.AggregatedActivityCount;
import io.getstream.core.options.PinActivityOption;
import io.getstream.core.options.UnpinActivityOption;
import io.getstream.core.options.UpdateToTargetsOption;
import java.io.IOException;
import java8.util.concurrent.CompletableFuture;
import java8.util.function.Function;
import java8.util.stream.Collectors;
import java8.util.stream.StreamSupport;

/**
 * Activities are the core object in Stream, they represent what your users do.
 *
 * <p>Activities are created by your users and aggregated in feeds. Feeds can be flat feeds,
 * aggregated feeds or notification feeds. Feeds and Activities are the core concepts to grasp.
 */
public final class Activity extends BaseActivity implements StreamObject {
  private static final long serialVersionUID = 1;

  /** create a new activity, the activity needs at least an actor, verb and object */
  public Activity(String actor, String verb, String object) {
    InitFields
