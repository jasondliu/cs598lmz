import io.reactivex.schedulers.Schedulers;

/**
 * Created by Administrator on 2017/6/30 0030.
 */

public class AppointmentPresenter {
    private final AppointmentModel model;
    private final AppointmentView view;

    public AppointmentPresenter(AppointmentView view) {
        this.model = new AppointmentModel();
        this.view = view;
    }

    public void getData(String uid, String token, String appoint_id) {
        model.getData(uid, token, appoint_id)
                .subscribeOn(Schedulers.io())
                .observeOn(AndroidSchedulers.mainThread())
                .subscribe(new Observer<AppointmentBean>() {
                    @Override
                    public void onSubscribe(Disposable d) {

                    }

                    @Override
                    public void onNext(AppointmentBean appointmentBean) {
                        view.showData(appointmentBean);
                    }

                    @Override
                    public void onError(Throwable e) {
                        view.show
