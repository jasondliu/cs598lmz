import io.reactivex.functions.BiFunction;
import io.reactivex.functions.Consumer;
import io.reactivex.schedulers.Schedulers;

/*
* 作者：zyq on 2018/12/31 15:58
* 邮箱：zyq@posun.com
*/
public class Rxjava2Manager {
    private static Rxjava2Manager rxjava2Manager;
    public static Rxjava2Manager getIntance(){
        if (rxjava2Manager==null){
            synchronized (Rxjava2Manager.class){
                if (rxjava2Manager==null){
                    rxjava2Manager=new Rxjava2Manager();
                }
            }
        }
        return rxjava2Manager;
    }
    public <T> void  get(String url, final Class<T> tClass, final HttpCallBack<T> httpCallBack){
        Observable.zip(Observable.create(new ObservableOnSubscribe<String>() {
            @Override
            public void subscribe(Observ
