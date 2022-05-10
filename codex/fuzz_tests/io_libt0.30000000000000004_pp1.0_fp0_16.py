import io.reactivex.Observable;
import io.reactivex.ObservableSource;
import io.reactivex.android.schedulers.AndroidSchedulers;
import io.reactivex.functions.Function;
import io.reactivex.schedulers.Schedulers;

/**
 * Created by Administrator on 2017/7/24.
 */

public class MyFragment extends Fragment {
    private View view;
    private RecyclerView mRecyclerView;
    private List<String> mList = new ArrayList<>();
    private MyAdapter mMyAdapter;
    private int mPage = 1;
    private int mCount = 10;
    private int mTotal = 0;
    private boolean isLoadMore = false;

    @Nullable
    @Override
    public View onCreateView(LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        view = inflater.inflate(R.layout.fragment_my, container, false);
        initView();
       
