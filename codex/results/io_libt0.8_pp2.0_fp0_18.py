import io.reactivex.Observable;
import okhttp3.ResponseBody;
import retrofit2.http.GET;

/**
 * Created by 俊杰 on 2017/3/3.
 */

public interface DownApi {
    @GET("http://downapk.xm12t.com/apk/17/1069/mimo.apk")
    Observable<ResponseBody> downlaod();
}
