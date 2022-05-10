import io.reactivex.disposables.Disposable;
import io.reactivex.functions.Consumer;

public class AccountDetailsFragment extends Fragment implements AccountDetailsView {

    @BindView(R.id.account_details_recycler_view)
    RecyclerView recyclerView;

    @BindView(R.id.account_details_refresh_layout)
    SwipeRefreshLayout refreshLayout;

    @BindView(R.id.account_details_progress_bar)
    ProgressBar progressBar;

    @BindView(R.id.account_details_error_text_view)
    TextView errorTextView;

    private AccountDetailsPresenter presenter;

    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.fragment_account_details, container, false);
        ButterKnife.bind(this, view);

        init();
        return view;
    }

    private void init() {

