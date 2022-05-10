import io.reactivex.Observable;
import retrofit2.http.GET;
import retrofit2.http.Query;

/**
 * Created by Administrator on 2018/1/4 0004.
 */

public interface ApiService {
    @GET("/toutiao/index")
    Observable<NewsBean> getNews(@Query("type") String type, @Query("key") String key);
}
