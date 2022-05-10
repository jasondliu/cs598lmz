import io.reactivex.Observable;
import io.reactivex.schedulers.Schedulers;

/**
 * Created by mac on 16/04/2018.
 */

public class RxTutorial {

    //    @Test
    public void main() {
        Observable<String> observable = Observable.create(new ObservableOnSubscribe<String>() {
            @Override
            public void subscribe(ObservableEmitter<String> e) throws Exception {
                e.onNext("1");
                e.onComplete();
            }
        });
        observable.subscribe(new Observer<String>() {
            @Override
            public void onSubscribe(Disposable d) {
                System.out.println("onSubscribe");
            }

            @Override
            public void onNext(String s) {
                System.out.println("onNext");
                System.out.println(s);
            }

            @Override
            public void onError(Throwable e) {
                System.out.println("onError");
                e.printStackTrace();

