import io.reactivex.Observable;

/**
 * Created by pratama on 9/23/17.
 */

public interface MainActivityContract {

    interface View extends BaseView<Presenter> {
        void showLoading();

        void hideLoading();

        void showError(String error);

        void showMatchList(List<Match> matchList);

        void showMatchDetail(Match match);

        void showMatchDetail(String id);
    }

    interface Presenter extends BasePresenter {
        void loadMatchList();

        void loadMatchDetail(String id);
    }

    interface Interactor {
        Observable<List<Match>> getMatchList();

        Observable<Match> getMatchDetail(String id);

        void setMatchList(List<Match> matchList);

        void setMatchDetail(Match match);
    }

    interface InteractorOutput {
        void onGetMatchListSuccess(List<Match> matchList);

        void onGetMatchListFailed(String error);

        void onGetMatchDetailSuccess(Match match);

        void onGet
