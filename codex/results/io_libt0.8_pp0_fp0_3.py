import io.appium.java_client.android.AndroidElement;
import io.appium.java_client.android.AndroidKeyCode;

import static org.junit.Assert.assertTrue;

public class CheckFreeAppiumInstallationTest {

	private AndroidDriver<AndroidElement> driver;

	@Before
	public void setUp() throws MalformedURLException {
		// Set up desired capabilities and pass the Android app-activity and app-package to Appium
		DesiredCapabilities capabilities = new DesiredCapabilities();
		capabilities.setCapability("BROWSER_NAME", "Android");
		capabilities.setCapability("VERSION", "5.0.2");
		capabilities.setCapability("deviceName", "Android Emulator");
		capabilities.setCapability("platformName", "Android");
		capabilities.setCapability("appPackage", "com.example.android.apis");
		capabilities.setCapability("appActivity", "ApiDemos");

		driver = new AndroidDriver<>(new URL("http://0.0
