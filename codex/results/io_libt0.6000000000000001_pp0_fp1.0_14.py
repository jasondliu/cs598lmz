import io.reactivex.Observable
import io.reactivex.Single
import javax.inject.Inject

class NetworkRepository @Inject constructor(
    private val apiService: ApiService
) : Repository {
    override fun getAllArticles(page: Int, pageSize: Int): Observable<List<Article>> {
        return apiService.getAllArticles(page, pageSize)
            .flatMapObservable {
                if (it.isSuccessful) Observable.just(it.body()?.articles)
                else Observable.error(Throwable("Failed to retrieve data!"))
            }
    }

    override fun getArticleDetails(id: Int): Single<Article> {
        return apiService.getArticleDetails(id)
            .flatMap {
                if (it.isSuccessful) Single.just(it.body()?.article)
                else Single.error(Throwable("Failed to retrieve data!"))
            }
    }
}
