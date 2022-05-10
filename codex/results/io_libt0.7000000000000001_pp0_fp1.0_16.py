import io.reactivex.functions.Consumer;
import io.reactivex.functions.Function;
import io.reactivex.schedulers.Schedulers;

/**
 * Created by yinzh on 2018/8/27.
 */
public class HttpUtils {

    private static final int TIMEOUT = 3000;
    private static OkHttpClient client;

    public static final String BASE_URL = "http://47.92.170.92:8080/";
    public static Retrofit retrofit;
    private static ApiService apiService;

    public static ApiService getApiService() {
        if (apiService == null) {
            return getInstance();
        }
        return apiService;
    }

    public static ApiService getInstance() {
        if (retrofit == null) {
            retrofit = new Retrofit.Builder()
                    .baseUrl(BASE_URL)
                    .addConverterFactory(GsonConverterFactory.create())
                    .addCallAdapterFactory(RxJava2CallAdapterFactory.create())
                   
