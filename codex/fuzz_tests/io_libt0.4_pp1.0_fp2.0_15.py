import io.reactivex.Single
import retrofit2.http.GET
import retrofit2.http.Path
import retrofit2.http.Query

interface ApiService {

    @GET("search/repositories")
    fun searchRepositories(@Query("q") query: String,
                           @Query("sort") sort: String,
                           @Query("order") order: String,
                           @Query("page") page: Int,
                           @Query("per_page") per_page: Int): Single<SearchRepositoryResponse>

    @GET("repos/{owner}/{repo}")
    fun getRepository(@Path("owner") owner: String,
                      @Path("repo") repo: String): Single<Repository>

    @GET("repos/{owner}/{repo}/contributors")
    fun getContributors(@Path("owner") owner: String,
                        @Path("repo") repo: String): Single<List<Contributor>>

}
