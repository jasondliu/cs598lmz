import io.reactivex.Observable
import io.reactivex.subjects.BehaviorSubject
import io.reactivex.subjects.PublishSubject

@PublishedApi
internal const val DEFAULT_PAGE = 1

/**
 * Created by lizhaotailang on 2017/6/24.
 *
 * Convert the [LiveData] to the [Observable] which could be used in RxJava2.
 */
internal fun <T> LiveData<T>.toObservable(): Observable<T> {
    return Observable.create { emitter ->
        val observable = Observer<T> {
            if (!emitter.isDisposed) {
                emitter.onNext(it)
            }
        }
        observeForever(observable)
        emitter.setCancellable {
            object : MainThreadDisposable() {
                override fun onDispose() {
                    removeObserver(observable)
                }
 
