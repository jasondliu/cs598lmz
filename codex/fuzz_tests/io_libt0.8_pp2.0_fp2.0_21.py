import io.realm.Realm;
import io.realm.RealmQuery;
import io.realm.RealmResults;

public class KaryawanFragment extends Fragment {
    Realm realm;
    RecyclerView recyclerView;
    RealmQuery query;
    RealmResults<Karyawan> karyawans;
    KaryawanAdapter adapter;
    @Nullable
    @Override
    public View onCreateView(LayoutInflater inflater, @Nullable ViewGroup container, Bundle savedInstanceState) {
        realm = Realm.getDefaultInstance();
        realm.setAutoRefresh(true);
        getActivity().setTitle("Data Karyawan");
        return inflater.inflate(R.layout.fragment_karyawan,container,false);
    }

    @Override
    public void onViewCreated(View view, @Nullable Bundle savedInstanceState) {
        super.onViewCreated(view, savedInstanceState);
        recyclerView = view.findViewById(R.id.rv_karyawan);
        recyclerView.setLayoutManager
