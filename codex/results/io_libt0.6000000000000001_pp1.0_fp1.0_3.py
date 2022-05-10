import io.reactivex.Observable
import retrofit2.http.Body
import retrofit2.http.GET
import retrofit2.http.POST
import retrofit2.http.Path

interface UserService {

    @GET("/users")
    fun getUsers(): Observable<List<User>>

    @GET("/users/{id}")
    fun getUser(@Path("id") id: Long): Observable<User>

    @POST("/users/register")
    fun registerUser(@Body user: User): Observable<User>

    @POST("/users/login")
    fun loginUser(@Body user: User): Observable<User>
}
