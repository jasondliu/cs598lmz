import io.reactivex.schedulers.Schedulers;
import retrofit2.Retrofit;

public class HttpUtil {
    private static HttpUtil httpUtil;
    private static Retrofit retrofit;

    private static final String baseUrl = "https://www.wanandroid.com";

    private HttpUtil() {
        retrofit = new Retrofit.Builder()
                .baseUrl(baseUrl)
                .addCallAdapterFactory(RxJava2CallAdapterFactory.create())
                .addConverterFactory(GsonConverterFactory.create())
                .client(new OkHttpClient())
                .build();
    }

    public static HttpUtil getInstance() {
        if (httpUtil == null) {
            synchronized (HttpUtil.class) {
                if (httpUtil == null) {
                    httpUtil = new HttpUtil();
                }
            }
        }
        return httpUtil;
    }

    public void getArticle(final HttpListener listener) {
        retrofit.create(Http
