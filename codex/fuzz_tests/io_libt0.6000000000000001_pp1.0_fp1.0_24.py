import io.reactivex.Observable
import io.reactivex.subjects.PublishSubject
import java.lang.NullPointerException

class RxBus {

    private val bus = PublishSubject.create<Any>()
    fun send(o: Any){
        bus.onNext(o)
    }

    fun toObservable(): Observable<Any> {
        return bus
    }

    fun hasObservers(): Boolean {
        return bus.hasObservers()
    }

    // this is to help with the NullPointerException issue
    // when checking if there are observers
    // since hasObservers() returns false if there are no observers
    fun <T> toObservable(eventType: Class<T>): Observable<T> {
        return bus.ofType(eventType)
    }

    fun hasObserverForEvent(eventType: Class<*>): Boolean {
        val observable = toObservable(eventType)
        return observable.hasObservers()
    }
}
