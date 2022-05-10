import io.reactivex.Single
import org.junit.jupiter.api.Assertions.assertEquals
import org.junit.jupiter.api.Test

internal class Test {

    @Test
    fun `test single`() {
        val single: Single<Int> = Single.just(1)
        val result = single.test()
        result.assertComplete()
        result.assertNoErrors()
        result.assertValue(1)
    }

    @Test
    fun `test single error`() {
        val single: Single<Int> = Single.error(Exception("error"))
        val result = single.test()
        result.assertError(Exception::class.java)
        result.assertErrorMessage("error")
    }

    @Test
    fun `test observable`() {
        val observable: Observable<Int> = Observable.just(1, 2, 3)
        val result = observable.test()
        result.assertComplete()
        result.assertNoErrors()
        result.assertValues(1, 2, 3)
    }

   
