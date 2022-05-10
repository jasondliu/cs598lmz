import io.reactivex.Observable
import io.reactivex.ObservableEmitter
import io.reactivex.ObservableOnSubscribe
import io.reactivex.android.schedulers.AndroidSchedulers
import io.reactivex.schedulers.Schedulers

/**
 * @author zhouchao
 * @date 2019/11/1
 */
class RxUtils {


    companion object {
        @JvmStatic
        fun <T> io2Main(observable: Observable<T>): Observable<T> =
            observable.subscribeOn(Schedulers.io())
                .observeOn(AndroidSchedulers.mainThread())


        @JvmStatic
        fun <T> createData(t: T): Observable<T> =
            Observable.create(ObservableOnSubscribe<T> { e ->
                try {
                    e.onNext(t)
                    e.onComplete()
                } catch (e1: Exception) {
                    e.onError(e1)

