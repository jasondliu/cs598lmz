import io.reactivex.schedulers.Schedulers;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;
import retrofit2.Retrofit;
import retrofit2.adapter.rxjava2.RxJava2CallAdapterFactory;
import retrofit2.converter.gson.GsonConverterFactory;

/**
 * @author: zhuhuanhuan
 * @time: 16/8/1-下午1:44.
 * @email: zhuhuanhuan@ushaqi.com
 * @desc:
 */
public class RetrofitUtils {

  private static RetrofitUtils mInstance;
  private Retrofit mRetrofit;
  private OkHttpClient mClient;

  private RetrofitUtils() {
    mClient = new OkHttpClient();
    mRetrofit = new Retrofit.Builder()
        .baseUrl("http://www.ushaqi.com/")
        .addConverterFactory(GsonConverterFactory.create())

