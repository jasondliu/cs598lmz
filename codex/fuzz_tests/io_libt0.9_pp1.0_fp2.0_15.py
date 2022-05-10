import io.appium.java_client.MobileBy;
import io.appium.java_client.android.AndroidDriver;
import io.appium.java_client.android.AndroidElement;
import io.appium.java_client.remote.MobileCapabilityType;

public class App extends Base {

	public static void main(String[] args) throws MalformedURLException {
		
		AndroidDriver<AndroidElement> driver = Capabilities();
//		driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);
//		driver.findElementByXPath("//android.widget.TextView[@text='Preference']").click();
		driver.findElementByXPath(" //android.widget.TextView[@text='Views']").click();
		//driver.findElement(By.xpath("//android.widget.TextView[@text='Views']")).click();
		driver.findElement(MobileBy.AndroidUIAutomator("text(\"WebView\")")).click();
		driver.find
