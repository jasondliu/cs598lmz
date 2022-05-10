import io.reactivex.schedulers.Schedulers


class MainViewModel constructor(
    app:Application,
    private val service: ProjectService
) : AndroidViewModel(app) {

    private val disposable = CompositeDisposable()

    private val _loading = MutableLiveData<Boolean>(false)
    val loading: LiveData<Boolean>
        get() = _loading

    private val _repoList = MutableLiveData<List<Repo>>()
    val repoList:LiveData<List<Repo>>
        get() = _repoList

    init {
        _repoList.value = emptyList()
        getRepoList()
    }

    fun getRepoList(){
        disposable.add(
            service.getRepoList()
                .subscribeOn(Schedulers.io())
                .observeOn(AndroidSchedulers.mainThread())
                .doOnSubscribe { _loading.postValue(true) }
                .
