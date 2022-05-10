import io.reactivex.Observable
import io.reactivex.Single
import io.reactivex.android.schedulers.AndroidSchedulers
import io.reactivex.disposables.Disposable
import io.reactivex.schedulers.Schedulers
import io.reactivex.subjects.PublishSubject
import io.reactivex.subjects.Subject
import java.util.*
import java.util.concurrent.TimeUnit

class MainViewModel(
    val repository: Repository,
    val schedulers: SchedulerProvider
) : ViewModel() {

    private val _state = MutableLiveData<MainViewState>()
    val state: LiveData<MainViewState> = _state

    private var disposable: Disposable? = null

    private val subject: Subject<Long> = PublishSubject.create<Long>()

    init {
        _state.value = MainViewState()
        init()
    }

    private fun init() {
        disposable = subject
            .observeOn(schedulers.
