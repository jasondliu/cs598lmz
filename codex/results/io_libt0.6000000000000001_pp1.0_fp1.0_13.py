import io.reactivex.Single
import retrofit2.http.GET
import retrofit2.http.Path
import retrofit2.http.Query

interface Api {

    @GET("breeds/list/all")
    fun getBreedList(): Single<BreedListResponse>

    @GET("breed/{breed}/images")
    fun getBreedImages(@Path("breed") breed: String,
                       @Query("limit") limit: Int): Single<BreedImagesResponse>
}
