import io.realm.RealmConfiguration;
import io.realm.RealmResults;

public class EpisodeFragment extends Fragment implements EpisodePresenter.View {

    public static String BASE_URL = "http://api.tvmaze.com";

    @BindView(R.id.rv_episode)
    RecyclerView recyclerView;

    @BindView(R.id.tv_heading)
    TextView heading;

    @BindView(R.id.tv_not_found)
    TextView notFound;

    @BindView(R.id.progress)
    ProgressBar progressBar;

    private Context context;
    private Realm realm;
    private EpisodeAdapter adapter;
    //private List<EpisodeModel> episodeList = new ArrayList<>();

    public EpisodeFragment(){
    }

    @Override
    public void onAttach(Context context) {
        super.onAttach(context);
        this.context = context;
        realm = Realm.getDefaultInstance();
    }

    @Override
    public void onCreate(@Nullable Bundle savedInstanceState) {
