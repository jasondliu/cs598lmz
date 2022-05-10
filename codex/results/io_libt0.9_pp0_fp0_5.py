import io.reactivex.disposables.Disposable;
import io.reactivex.functions.Consumer;
import io.reactivex.schedulers.Schedulers;

/**
 * @Auther: liziyang
 * @datetime: 2019-11-24
 * @desc:
 */
public class DataManager {

    private static RetrofitService mApiService;
    private static DataManager instance;

    private DataManager(){

    }

    public static DataManager getInstance(Context context){
        if (instance == null){
            synchronized (DataManager.class){
                if (instance == null){
                    instance = new DataManager();
                    initOkHttpClient(context);
                }
            }
        }
        return instance;
    }

    private static void initOkHttpClient(Context context) {
        ArrayList<Interceptor> interceptors = new ArrayList<>();
        // 基本的拦截器
        BasicParamsInterceptor paramsInterceptor = new BasicParamsInterceptor.Builder()
                .addQueryParam
