import io.reactivex.Observable
import io.reactivex.ObservableSource
import io.reactivex.ObservableTransformer
import io.reactivex.functions.BiFunction
import io.reactivex.functions.Function
import io.reactivex.functions.Predicate
import io.reactivex.schedulers.Schedulers
import kotlinx.coroutines.runBlocking
import org.junit.Test
import java.util.concurrent.TimeUnit

/**
 * @author wangzhichao
 * @date 2019/10/20
 */
class Test3 {
    @Test
    fun test1() {
        // 创建一个发射整数的 Observable
        val observable = Observable.create<Int> { emitter ->
            println("create: ${Thread.currentThread().name}")
            emitter.onNext(1)
            emitter.onNext(2)
            emitter.onNext(3)
            emitter.onComplete()
        }
