import io.reactivex.Observable;
import io.reactivex.Observer;

/**
 * Created by Administrator on 2017/9/13.
 */

public class RxRetrofitHelper {
    private static RxRetrofitHelper instance = null;

    private Retrofit retrofit = null;
    private Context context = null;
    private RxRetrofitService rxRetrofitService = null;

    public static RxRetrofitHelper getInstance(Context context) {
        if (instance == null) {
            instance = new RxRetrofitHelper(context);
        }
        return instance;
    }

    private RxRetrofitHelper(Context context) {
        this.context = context;
        init();
    }

    private void init() {
        OkHttpClient.Builder builder = new OkHttpClient.Builder();
        if (Constants.isDebug) {
            builder.addInterceptor(new LogInterceptor());
        }
        builder.connectTimeout(Constants.DEFAULT_TIMEOUT, TimeUnit.SECONDS);
        builder.readTimeout(Constants.
