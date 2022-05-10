import io.reactivex.Observable;
import io.reactivex.android.schedulers.AndroidSchedulers;
import io.reactivex.schedulers.Schedulers;
import utils.HttpUrl.URL;

public class MiningFragment extends Fragment{

    private TextView tv_balance_mining_fragment;

    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.fragment_mining, container, false);

        tv_balance_mining_fragment = view.findViewById(R.id.tv_balance_mining_fragment);

        getBalance();

        return view;
    }

    private void getBalance() {

        SharedPreferences sharedPreferences = getActivity().getSharedPreferences(URL.PREF, Context.MODE_PRIVATE);

        String address = sharedPreferences.getString("address", "");

       
