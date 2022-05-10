import io.reactivex.schedulers.Schedulers

class ProfileViewModel : ViewModel() {

    private var mutableUserCard = MutableLiveData<UserCard>()
    private var mutableProfilePhoto = MutableLiveData<ProfilePhoto>()

    fun getUserCardLiveData(): MutableLiveData<UserCard> {
        return mutableUserCard
    }

    fun getProfilePhotoLiveData(): MutableLiveData<ProfilePhoto> {
        return mutableProfilePhoto
    }

    fun getProfile(id: String) {
        mLiveChatApi.getUserCard(id)
            .subscribeOn(Schedulers.io())
            .observeOn(AndroidSchedulers.mainThread())
            .subscribe(object : Observer<UserCard> {
                override fun onComplete() {

                }

                override fun onSubscribe(d: Disposable) {

                }

                override fun onNext(t: UserCard) {
                    mutableUserCard.value = t
                }

                override fun onError(e: Throwable) {


