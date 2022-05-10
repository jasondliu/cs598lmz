import io.reactivex.Observable;
import io.reactivex.Observer;
import io.reactivex.android.schedulers.AndroidSchedulers;
import io.reactivex.disposables.Disposable;
import io.reactivex.schedulers.Schedulers;
import okhttp3.Call;
import okhttp3.Callback;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;
import okhttp3.logging.HttpLoggingInterceptor;

/**
 * @author xts
 *         Created by asus on 2019/9/2.
 */

public class HttpUtils {
    public static final String sBaseUrl = "http://www.qubaobei.com/ios/cf/";
    private static volatile HttpUtils sHttpUtils;
    private final OkHttpClient mClient;

    HttpUtils() {
        HttpLoggingInterceptor interceptor = new HttpLoggingInterceptor();
        interceptor.setLevel(HttpLog
