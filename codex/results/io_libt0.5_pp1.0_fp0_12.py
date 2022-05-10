import io.reactivex.Observable
import retrofit2.http.GET
import retrofit2.http.Query

interface ApiService {
    @GET("/v1/gifs/search")
    fun getGifs(@Query("q") query: String,
                @Query("api_key") apiKey: String,
                @Query("limit") limit: Int,
                @Query("rating") rating: String,
                @Query("offset") offset: Int = 0): Observable<GifResponse>
}
