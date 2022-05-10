import io.reactivex.Observable
import io.reactivex.disposables.CompositeDisposable
import io.reactivex.disposables.Disposable
import io.reactivex.functions.Consumer
import io.reactivex.rxkotlin.plusAssign
import io.reactivex.rxkotlin.subscribeBy
import io.reactivex.schedulers.Schedulers
import java.util.concurrent.TimeUnit
import javax.inject.Inject

/**
 * @author Anton Kirichenkov
 */
class MainPresenter @Inject constructor() : BasePresenter<MainView>() {

    @Inject
    lateinit var api: Api

    private var currentPage = 1
    private var totalPages = 1
    private var isLoading = false

    private val compositeDisposable = CompositeDisposable()

    override fun onViewAttached() {
        super.onViewAttached()

        getMovies()
        getPopularMovies()
    }

    private fun getMovies() {

