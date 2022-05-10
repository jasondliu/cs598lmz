import io.reactivex.Observable
import retrofit2.http.GET

/**
 * Created by Darshan Patel 24/02/2020
 * Usage: Api for getting list of subcategories
 * How to call: This class will be called from ListingFragment
 * Useful parameter:
 */
interface SubCategoryListApi {

    @GET("/api/v1/categories/2/subcategories")
    fun getSubCategories(): Observable<List<SubCategoryResponse>>
}
