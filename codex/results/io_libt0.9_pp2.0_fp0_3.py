import io.reactivex.Observable;
import io.reactivex.ObservableEmitter;
import io.reactivex.ObservableOnSubscribe;
import io.reactivex.android.schedulers.AndroidSchedulers;
import io.reactivex.schedulers.Schedulers;

/**
 * Created by qiang on 2018/12/27.
 */

public class ScreenCheckModel implements ScreenCheckContract.ScreenCheckModel {


    @Override
    public void getScreenCheckInfo(String ScreenCode, final OnCallBack onCallBack) {
        Observable.create(new ObservableOnSubscribe<ScreenCheckRespBean>() {
            @Override
            public void subscribe(@NonNull ObservableEmitter<ScreenCheckRespBean> e) throws Exception {
                ScreenCheckRespBean screenCheckRespBean = new ScreenCheckRespBean();
                screenCheckRespBean.setStatus("0");
                screenCheckRespBean.setDescription("成功");
                screenCheckRespBean.setScreenName("屏显01");
