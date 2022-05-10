import io.reactivex.Observable;
import retrofit2.http.Field;
import retrofit2.http.FormUrlEncoded;
import retrofit2.http.POST;

/**
 * Created by Administrator on 2017/10/31.
 */

public interface UpdateService {
    @FormUrlEncoded
    @POST("app/updateVersion")
    Observable<BaseResponse<UpdateBean>> update(@Field("version") String version, @Field("type") int type);
}
