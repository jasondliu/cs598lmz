import io.reactivex.Single
import io.reactivex.android.schedulers.AndroidSchedulers
import io.reactivex.schedulers.Schedulers
import javax.inject.Inject

class GooglePlayRepository @Inject constructor(
        val googlePlayService: GooglePlayService,
        val extractor: AppReleasesExtractor
): AppReleasesRepository {
    override fun getAppReleases(packageName: String): Single<List<GitHubRelease>> {
        return googlePlayService.releases(packageName, Locale.getDefault().language)
                .subscribeOn(Schedulers.io())
                .observeOn(AndroidSchedulers.mainThread())
                .map(extractor::extract)
    }
}
