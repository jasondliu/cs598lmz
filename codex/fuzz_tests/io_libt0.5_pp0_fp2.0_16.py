import io.reactivex.Observable
import io.reactivex.android.schedulers.AndroidSchedulers
import io.reactivex.disposables.Disposable
import io.reactivex.subjects.PublishSubject
import java.util.concurrent.TimeUnit

class SearchResultViewModel(
    private val repository: Repository,
    private val searchSubject: PublishSubject<String>
) : ViewModel() {

    private var disposable: Disposable? = null

    private val searchResult = MutableLiveData<List<SearchResult>>()

    init {
        disposable = searchSubject
            .debounce(300, TimeUnit.MILLISECONDS)
            .distinctUntilChanged()
            .switchMap {
                repository.search(it)
                    .subscribeOn(Schedulers.io())
                    .observeOn(AndroidSchedulers.mainThread())
                    .onErrorReturn { emptyList() }
            }
            .subscribe { searchResult.value = it }
    }

    fun search(query: String)
