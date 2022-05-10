import io.vlingo.symbio.store.state.jdbc.JdbcStorageDelegate;

public abstract class JdbcQueryModelStore<T extends QueryModel> extends JdbcStateStore implements QueryModelStore<T> {
  private final Dispatcher dispatcher;
  private final QueryModelDispatcher<T> modelDispatcher;
  private final Metadata metadata;
  private final String persistentType;
  private final StateAdapterProvider stateAdapterProvider;
  
  protected JdbcQueryModelStore(
          final JdbcStateStoreConfiguration configuration,
          final StateAdapterProvider stateAdapterProvider,
          final String persistentType,
          final Dispatcher dispatcher,
          final QueryModelDispatcher<T> modelDispatcher,
          final Metadata metadata) {
    super(configuration);
    this.dispatcher = dispatcher;
    this.modelDispatcher = modelDispatcher;
    this.metadata = metadata;
    this.persistentType = persistentType;
    this.stateAdapterProvider = stateAdapterProvider;
  }

  protected abstract JdbcStorageDelegate
