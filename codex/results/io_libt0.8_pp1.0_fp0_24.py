import io.reactivex.disposables.CompositeDisposable;
import io.reactivex.observers.DisposableObserver;
import io.reactivex.schedulers.Schedulers;
import okhttp3.Call;
import okhttp3.Response;
import okhttp3.ResponseBody;
import retrofit2.Retrofit;
import retrofit2.adapter.rxjava2.RxJava2CallAdapterFactory;
import retrofit2.converter.gson.GsonConverterFactory;
import retrofit2.converter.scalars.ScalarsConverterFactory;

import static org.apache.http.HttpHeaders.ACCEPT;
import static org.apache.http.HttpHeaders.USER_AGENT;

public class MainActivity extends AppCompatActivity implements View.OnClickListener {

    private SyncHttpClient syncHttpClient;
    private AsyncHttpClient asyncHttpClient;
    private int mHttpCode = 0;
    private Toolbar mToolbar;
    private Button mOneButton;
    private Button m
