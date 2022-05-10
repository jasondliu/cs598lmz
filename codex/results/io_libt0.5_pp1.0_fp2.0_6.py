import io.reactivex.Single

class SearchRepository(private val api: Api) {

    fun search(query: String): Single<List<SearchResponse>> {
        return api.search(query)
    }
}
