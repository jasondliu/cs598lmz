import io.reactivex.Observable
import io.reactivex.ObservableSource
import io.reactivex.functions.BiFunction
import io.reactivex.functions.Function
import io.reactivex.schedulers.Schedulers
import java.util.concurrent.TimeUnit

class RxJavaTest {

    companion object {
        fun test() {
            val rxJavaTest = RxJavaTest()
            rxJavaTest.test1()
        }
    }

    private fun test1() {
        Observable.just(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
                .subscribeOn(Schedulers.io())
                .observeOn(Schedulers.newThread())
                .flatMap(object : Function<Int, ObservableSource<Int>> {
                    override fun apply(t: Int): ObservableSource<Int> {
                        return Observable.just(t)
                    }
                })
                .filter(object : Predicate<Int> {
                    override fun test(
