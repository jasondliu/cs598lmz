import io.flutter.plugin.common.MethodChannel;

public class MainActivity extends FlutterActivity {
  @Override
  public void configureFlutterEngine(@NonNull FlutterEngine flutterEngine) {
    super.configureFlutterEngine(flutterEngine);

    new MethodChannel(flutterEngine.getDartExecutor().getBinaryMessenger(), "com.example.test")
      .setMethodCallHandler(new MethodChannel.MethodCallHandler() {
        @Override
        public void onMethodCall(@NonNull MethodCall call, @NonNull MethodChannel.Result result) {
          if (call.method.equals("getBatteryLevel")) {
            int batteryLevel = getBatteryLevel();

            if (batteryLevel == -1) {
              result.error("UNAVAILABLE", "Could not fetch battery level", null);
            } else {
              result.success(batteryLevel);
            }
          } else {
            result.notImplemented();
          }
        }
      });
  }

  private int getBatteryLevel() {
    int batteryLevel = -1
