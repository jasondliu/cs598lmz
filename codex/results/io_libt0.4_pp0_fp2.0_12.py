import io.reactivex.schedulers.Schedulers;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import retrofit2.Retrofit;
import retrofit2.adapter.rxjava2.RxJava2CallAdapterFactory;
import retrofit2.converter.gson.GsonConverterFactory;
import retrofit2.converter.scalars.ScalarsConverterFactory;

/**
 * Created by Administrator on 2018/3/13.
 */

public class RetrofitHelper {

    private static OkHttpClient okHttpClient;
    private static ApiService apiService;

    static {
        initOkHttpClient();
    }

    public static ApiService getApiService() {
        if (apiService == null) {
            synchronized (RetrofitHelper.class) {
                apiService = onCreateApi(ApiService.class, Api.BASE_URL);
            }
        }
        return apiService;
    }

    private static <T> T onCreateApi(Class<
