import io.reactivex.Observable

interface SearchRepository {
    fun searchMovie(apiKey: String, query: String, page: Int): Observable<SearchMoviesResponse>
    fun searchTvShow(apiKey: String, query: String, page: Int): Observable<SearchTvShowResponse>
    fun searchPerson(apiKey: String, query: String, page: Int): Observable<SearchPersonResponse>
}
