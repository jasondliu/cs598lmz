import io.realm.Realm
import io.realm.RealmQuery
import io.realm.RealmResults
import io.realm.Sort
import io.realm.kotlin.where
import java.util.*

class MainViewModel(application: Application) : AndroidViewModel(application) {
    private val realm: Realm = Realm.getDefaultInstance()
    private val repository = RealmRepository(realm)

    val allGoods: RealmResults<Goods> = repository.findAllGoods()
    val allSales: RealmResults<Sales> = repository.findAllSales()
    val allGoodsWithSales: RealmResults<Goods> = repository.findAllGoodsWithSales()

    private val _showProgressBar = MutableLiveData<Boolean>()
    val showProgressBar: LiveData<Boolean>
        get() = _showProgressBar

    private val _showSnackbar = MutableLiveData<String>()
    val showSnackbar: LiveData<String>
        get() = _showSnackbar

    private val _showFab = MutableLiveData
