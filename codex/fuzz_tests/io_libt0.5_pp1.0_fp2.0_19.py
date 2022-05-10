import io.reactivex.Observable;
import retrofit2.Response;
import retrofit2.http.GET;
import retrofit2.http.Query;

/**
 * Created by sachin on 16/3/18.
 */

public interface ApiInterface {

    @GET("v1/search")
    Observable<Response<SearchResponse>> getSearchResults(@Query("term") String term, @Query("entity") String entity);
}
