import io.reactivex.Observable;

/**
 * Created by jp on 2018/6/7.
 */

public class MainModel implements MainContract.Model {

    @Override
    public Observable<String> getData() {
        return Observable.just("Hello World");
    }
}
