import io.reactivex.Observable
import io.reactivex.disposables.CompositeDisposable
import io.reactivex.disposables.Disposable
import io.reactivex.rxkotlin.addTo
import io.reactivex.subjects.BehaviorSubject
import io.reactivex.subjects.PublishSubject
import io.reactivex.subjects.Subject
import java.util.concurrent.TimeUnit

class MainViewModel(
    private val repository: Repository,
    private val schedulerProvider: SchedulerProvider
) : ViewModel() {

    private val compositeDisposable = CompositeDisposable()

    private val _state = BehaviorSubject.create<State>()
    val state: Observable<State> = _state

    private val _event = PublishSubject.create<Event>()
    val event: Observable<Event> = _event

    private val _action = PublishSubject.create<Action>()
    val action: Observable<Action> = _action

    private val _intent = PublishSubject.create<Int
