import io.reactivex.Observable;
import io.reactivex.ObservableEmitter;
import io.reactivex.ObservableOnSubscribe;
import io.reactivex.Observer;
import io.reactivex.disposables.Disposable;
import io.reactivex.functions.Consumer;

/**
 * Created by sunfusheng on 2017/6/20.
 */
public class RecyclerViewActivity extends BaseActivity {

    private RecyclerView recyclerView;
    private RecyclerViewAdapter adapter;
    private List<String> items = new ArrayList<>();

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_recycler_view);

        initData();
        initView();

        tesRxjava();
    }

    private void tesRxjava(){
        Observable.create(new ObservableOnSubscribe<String>() {
            @Override
            public void subscribe(Observ
