import io.vlingo.symbio.store.state.StateStore.WriteResultInterest;
import io.vlingo.symbio.store.state.StateStore.Writer;
import io.vlingo.symbio.store.state.StateTypeStateStoreMap;

/**
 * In memory {@link StateStore} implementation.
 */
public class InMemoryStateStoreActor extends Actor implements StateStore, WriteResultInterest {
  private final StateStore.WriteResultInterest interest;
  private final StateTypeStateStoreMap stateTypeStateStoreMap;
  private final StateStoreDelegate stateStoreDelegate;

  /**
   * Constructs an instance of {@link InMemoryStateStoreActor}
   * @param name the name of the {@link InMemoryStateStoreActor}
   * @param interest the {@link WriteResultInterest}
   */
  public InMemoryStateStoreActor(final String name, final WriteResultInterest interest) {
    this.interest = interest;
    this.stateTypeStateStoreMap = StateTypeStateStoreMap.of(stage().world().defaultLogger());
    this.stateStoreDe
