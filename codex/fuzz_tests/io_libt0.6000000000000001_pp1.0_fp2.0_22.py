import io.reactivex.Observable
import io.reactivex.Single
import io.reactivex.schedulers.Schedulers
import java.util.concurrent.TimeUnit
import javax.inject.Inject

class RepositoryImpl
@Inject constructor(
    private val local: Local,
    private val remote: Remote,
    private val scheduler: SchedulerProvider
) : Repository {

    override fun getAvailableCurrencies(): Observable<List<Currency>> {
        return remote.getAvailableCurrencies()
            .subscribeOn(scheduler.io())
    }

    override fun getRates(baseCurrency: String): Observable<List<CurrencyRate>> {
        return remote.getRates(baseCurrency)
            .subscribeOn(scheduler.io())
            .map { it.toCurrencyRateList() }
            .doOnNext {
                local.saveCurrencyRates(it)
            }
    }

    override fun getLocalRates(): Observable<List<CurrencyRate>> {
        return
