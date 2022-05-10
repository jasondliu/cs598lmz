import io.reactivex.android.schedulers.AndroidSchedulers;
import io.reactivex.disposables.CompositeDisposable;
import io.reactivex.disposables.Disposable;
import io.reactivex.schedulers.Schedulers;

public class MainActivity extends AppCompatActivity implements MainView {

    private RecyclerView rvNews;
    private NewsAdapter adapter;
    private MainPresenter presenter;
    private CompositeDisposable compositeDisposable;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        compositeDisposable = new CompositeDisposable();
        initViews();
        initPresenter();
    }

    private void initPresenter() {
        presenter = new MainPresenter(this, compositeDisposable);
        presenter.getNews();
    }

    private void initViews() {
        rvNews = findViewById(R.id.rv
