import io.reactivex.functions.Consumer;

public class MyApp extends Application {

    private static final String TAG = "MyApp";

    @Override
    public void onCreate() {
        super.onCreate();

        //初始化全局异常捕获
        CrashReport.initCrashReport(getApplicationContext(), "a0cdf60dcf", false);

        //初始化数据库
        FlowManager.init(this);

        //初始化Bugly
        initBugly();
    }

    private void initBugly() {
        //获取当前包名
        String packageName = this.getPackageName();
        //获取当前进程名
        String processName = getProcessName(android.os.Process.myPid());
        //设置是否为上报进程
        CrashReport.UserStrategy strategy = new CrashReport
