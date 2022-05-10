import io.reactivex.Single;
import retrofit2.http.GET;
import retrofit2.http.Path;
import retrofit2.http.Query;

public interface ApiService {

    @GET("users")
    Single<List<User>> getUsers(@Query("page") int page, @Query("per_page") int perPage);

    @GET("users/{id}")
    Single<User> getUser(@Path("id") long userId);
}
