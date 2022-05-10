import io.reactivex.Observable;
import retrofit2.http.Body;
import retrofit2.http.POST;

/**
 * Created by Administrator on 2018/3/9.
 */

public interface LoginService {

    @POST("/api/v1/user/login")
    Observable<User> login(@Body User user);

}
