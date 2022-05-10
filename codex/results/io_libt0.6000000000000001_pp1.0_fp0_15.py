import io.reactivex.Observable
import io.reactivex.functions.BiFunction
import java.util.concurrent.TimeUnit

/**
 * Created by Administrator on 2017/12/18.
 */
class RxZip {

    fun zipDemo(){

        Observable.zip(Observable.interval(1, TimeUnit.SECONDS).map { it.toString() }, Observable.just("a","b","c"),
                BiFunction<String, String, String> { t1, t2 -> t1 + " " + t2 })
                .subscribe { println("zip:$it") }

        Observable.zip(Observable.interval(1, TimeUnit.SECONDS).map { it.toString() }, Observable.just("a","b","c"),
                BiFunction<String, String, String> { t1, t2 -> t1 + " " + t2 })
                .subscribe { println("zip:$it") }

    }
}
