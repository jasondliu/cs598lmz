import io.realm.RealmObject;
import io.realm.RealmResults;

/**
 * Created by Raquel on 18/04/2018.
 */

public class RealmClienteRepository implements IClienteRepository {
    private final String TAG = this.getClass().getName();

    public IClienteService _ClienteService;
    public IClienteService GetClienteService() {
        return _ClienteService;
    }
    public void SetClienteService(IClienteService _ClienteService) {
        this._ClienteService = _ClienteService;
    }
    public RealmClienteRepository(Application application) {
        try {
            RealmRepository.initializeRealmConfig(application);
            SetClienteService(new ClienteService(RealmRepository.realmInstance));
        } catch (IOException ex) {
            Log.e(TAG, ex.getMessage());
        }
    }

    public RealmClienteRepository(Realm realm) {
        try {
            RealmRepository.realmInstance = realm;
            SetClient
