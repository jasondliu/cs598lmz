import io.appium.java_client.touch.WaitOptions;
import io.appium.java_client.touch.offset.ElementOption;

public class ScreenNotificationChartActivity extends AbstractBaseActivity {

	public static String TAG = "ScreenNotificationChartActivity";

	public static String quickAlertLocation = "android:id/mwQuickActions LinearLayout id:0";
	public static String sameDayLocation = "android:id/mwQuickActions LinearLayout id:1";

	// android:id/mwQuickActions LinearLayout id:1
	public static String titleQuickAlert = "Quick Alerts";
	public static String txtMessage = "Did you measure blood glucose?";
	public static String btnSkip = "SKIP";
	public static String btnSendData = "SEND DATA";
	//
	public static String btnNotification = "Notifications";

	public static String quickAlertTitle = "Quick Alert";
	public static String chosenQuickScreenQuantity = "120";
	public static String inputMessage = "Cause! Just a test!";
	public static String[] bloodValue = { "
