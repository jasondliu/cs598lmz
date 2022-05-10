import io.reactivex.schedulers.Schedulers

class SearchResultsViewModel @ViewModelInject constructor(
    private val repositories: Repositories,
    private val schedulers: SchedulerProvider
) : ViewModel() {

    private val isLoading = MutableLiveData<Boolean>()
    private val searchLiveData = MutableLiveData<SearchResult>()

    private val compositeDisposable = CompositeDisposable()

    fun loadSearchResults(query: String) {
        isLoading.value = true
        compositeDisposable.add(
            repositories.getGifs(query)
                .map {
                    SearchResult(0, it, null)
                }
                .onErrorReturn {
                    SearchResult(it, emptyList(), null)
                }
                .doFinally {
                    isLoading.value = false
                }
                .subscribeOn(schedulers.io())
                .observeOn(schedulers.ui())
                .subscribe {
                    searchLiveData.value = it
                }
        )
    }

   
