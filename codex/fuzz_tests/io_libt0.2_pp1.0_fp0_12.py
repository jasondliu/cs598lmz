import io.reactivex.Observable;
import io.reactivex.ObservableEmitter;
import io.reactivex.ObservableOnSubscribe;
import io.reactivex.Observer;
import io.reactivex.android.schedulers.AndroidSchedulers;
import io.reactivex.disposables.Disposable;
import io.reactivex.schedulers.Schedulers;

/**
 * Created by Administrator on 2017/12/27.
 */

public class RxJavaActivity extends AppCompatActivity {

    private static final String TAG = "RxJavaActivity";
    private Button btn_rxjava;
    private Button btn_rxjava_map;
    private Button btn_rxjava_flatmap;
    private Button btn_rxjava_concatmap;
    private Button btn_rxjava_zip;
    private Button btn_rxjava_combine;
    private Button btn_rxjava_filter;
    private Button btn_rxjava_distinct;
    private Button btn_rxjava_
