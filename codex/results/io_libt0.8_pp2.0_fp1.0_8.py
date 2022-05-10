import io.reactivex.Observable
import retrofit2.Call
import retrofit2.http.GET
import retrofit2.http.Path
import retrofit2.http.Query

/**
 * Created by Administrator on 2018/5/7.
 */
public interface RemoteService {
    @GET("/repos/{owner}/{repo}/contributors")
    fun getContributors(@Path("owner") owner: String, @Path("repo") repo: String): Observable<List<Contributor>>
    @GET("/search/repositories")
    fun searchRepositories(@Query("q") query: String, @Query("sort") sort: String, @Query("order") order: String) : Call<RepoSearchResponse>
    @GET("/users/{username}/repos")
    fun getRepo(@Path("username") username : String) : Call<List<Repo>>
}
