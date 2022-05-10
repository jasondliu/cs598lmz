import io.cordova.zhihuiyingyuan.utils.MyApp;
import io.cordova.zhihuiyingyuan.utils.SPUtils;

/**
 * Created by Administrator on 2019/4/19 0019.
 */

public class MyReceiver extends BroadcastReceiver {
    @Override
    public void onReceive(Context context, Intent intent) {
        String action = intent.getAction();
        if(action.equals("android.intent.action.BOOT_COMPLETED")){
            String isLogin = (String)SPUtils.get(MyApp.getInstance(),"isLogin","");
            if(isLogin.equals("1")){
                MyApp.getInstance().startMyService();
            }
        }
    }
}
