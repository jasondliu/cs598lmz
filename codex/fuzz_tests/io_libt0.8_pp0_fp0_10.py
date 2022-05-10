import io.reactivex.disposables.CompositeDisposable;
import io.reactivex.observers.DisposableObserver;

public class RecommendationPresenterImpl extends BasePresenterImpl<RecommendationView> implements RecommendationPresenter {
    private final CompositeDisposable compositeDisposable;
    private final RecommendationInteractor recommendationInteractor;

    public RecommendationPresenterImpl(RecommendationView view, RecommendationInteractor recommendationInteractor) {
        super(view);
        this.recommendationInteractor = recommendationInteractor;
        this.compositeDisposable = new CompositeDisposable();
    }

    @Override
    public void getRecommendations(String userId) {
        getView().showLoading();
        compositeDisposable.add(recommendationInteractor.getRecommendations(userId)
                .observeOn(AndroidSchedulers.mainThread())
                .subscribeWith(new DisposableObserver<RecommendationResponse>() {
                    @Override
                    public void onNext(RecommendationResponse recommendationResponse) {
                        getView().hide
