import io.reactivex.Observable
import io.reactivex.disposables.CompositeDisposable
import io.reactivex.rxkotlin.addTo
import io.reactivex.schedulers.Schedulers
import io.reactivex.subjects.BehaviorSubject
import io.reactivex.subjects.PublishSubject
import io.reactivex.subjects.Subject
import java.util.concurrent.TimeUnit

class RxBus {

    private val bus: Subject<Any> = PublishSubject.create<Any>().toSerialized()
    private val disposables = CompositeDisposable()

    fun post(event: Any) {
        bus.onNext(event)
    }

    fun <T> observe(eventType: Class<T>): Observable<T> {
        return bus.ofType(eventType)
    }

    fun <T> observe(eventType: Class<T>, debounceTime: Long = 500, unit: TimeUnit = TimeUnit.MILLISECONDS): Observable<T> {
       
