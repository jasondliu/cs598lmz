import io.reactivex.Observable
import io.reactivex.android.schedulers.AndroidSchedulers
import io.reactivex.disposables.Disposable
import io.reactivex.schedulers.Schedulers
import javax.inject.Inject

class MainPresenter @Inject constructor(
    private val localDataSource: LocalDataSource
) {

    private var disposable: Disposable? = null

    /**
     * Load data to MainActivity
     */
    fun loadData(loadData: (List<GitHubRepo>) -> Unit) {
        disposable = localDataSource.getRepositories()
            .subscribeOn(Schedulers.io())
            .observeOn(AndroidSchedulers.mainThread())
            .flatMap {
                Observable.fromCallable {
                    localDataSource.saveRepositories(it, true)
                    it
                }
            }
            .subscribe(
                { items ->
                    loadData.invoke(items)
                },
                {
                    it.
