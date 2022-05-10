import io.reactivex.Single
import io.reactivex.disposables.CompositeDisposable
import io.reactivex.schedulers.Schedulers
import java.util.*
import kotlin.collections.ArrayList

class ActivityMainViewModel : ViewModel() {

    private var compositeDisposable: CompositeDisposable = CompositeDisposable()
    private var repository: Repository = Repository()
    private var list: MutableLiveData<List<User>> = MutableLiveData()
    private var progressBar: MutableLiveData<Boolean> = MutableLiveData()
    private var sortedList: MutableLiveData<List<User>> = MutableLiveData()
    private var searchList: MutableLiveData<List<User>> = MutableLiveData()
    private var searchQuery: MutableLiveData<String> = MutableLiveData()
    private var isSorted: MutableLiveData<Boolean> = MutableLiveData()

    init {
        progressBar.value = false
        list.value = ArrayList()
        sortedList.
