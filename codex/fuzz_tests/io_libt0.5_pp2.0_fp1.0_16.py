import io.reactivex.Observable;
import io.reactivex.ObservableEmitter;
import io.reactivex.ObservableOnSubscribe;
import io.reactivex.functions.Consumer;
import io.reactivex.schedulers.Schedulers;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;
import retrofit2.Retrofit;
import retrofit2.adapter.rxjava2.RxJava2CallAdapterFactory;
import retrofit2.converter.gson.GsonConverterFactory;

public class RetrofitManager {
    //单例模式
    private static final String TAG = "RetrofitManager";
    private static volatile RetrofitManager mInstance;
    private Retrofit retrofit;
    private RetrofitService mRetrofitService;

    private RetrofitManager() {
        //初始化Retrofit
        retrofit = new Retrofit.Builder()
                .baseUrl(Constants.BASE_URL
