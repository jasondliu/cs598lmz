import io.reactivex.Single;

/**
 * Created by nguyenvanhien on 12/17/17.
 */

public interface DataManager {
    Single<List<User>> getUserList();
}
