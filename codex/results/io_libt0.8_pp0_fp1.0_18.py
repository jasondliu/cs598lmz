import io.reactivex.Completable
import io.reactivex.Observable
import io.reactivex.Single
import io.reactivex.subjects.BehaviorSubject
import io.reactivex.subjects.PublishSubject
import javax.inject.Inject

class FetchMerchantInfoUseCase @Inject constructor(
    private val merchantRepo: MerchantRepo,
    private val appInfo: AppInfo
) : ResultingUseCase<MerchantInfo, FetchMerchantInfoUseCase.Params>() {
    override val execute: (Params) -> Observable<Result<MerchantInfo>> = { params ->
        merchantRepo.acceptedMerchantMapper
            .getMerchantInfo(params.merchantCode)
            .toObservable()
            .doOnNext {
                analyticsEvent(contains(REQUIRED_FIELDS, it))
            }
            .flatMap {
                if (params.deepLink != null && params.deepLink.isNotEmpty()) {
                    merchantRepo
                        .acceptedMerchantMapper
