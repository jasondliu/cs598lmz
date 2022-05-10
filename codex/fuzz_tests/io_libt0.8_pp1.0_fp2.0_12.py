import io.reactivex.Flowable;
import io.reactivex.Single;
import io.reactivex.Completable;
import io.reactivex.Maybe;

/**
 * <p>
 * This is the only API entry point for performing CRUD operations on the user domain.
 * This should not be instantiated directly; instead, use the API client ({@link Client})
 * to get an instance of this class.
 * </p>
 */
@Api(
    name = "User",
    priority = Priority.P2,
    version = "v2",
    namespace = @ApiNamespace(ownerDomain = "com.expediagroup.graphql.plugin", ownerName = "Expediagroup")
)
public interface UserApi {
  /**
   * Create a User
   * 
   * @param input User to create (required)
   * @throws ApiException if fails to make API call
   */
  void createUser(User input) throws ApiException;
    
  /**
   * Create a User
   * 
   *
