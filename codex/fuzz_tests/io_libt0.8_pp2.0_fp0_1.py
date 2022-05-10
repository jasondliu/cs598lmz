import io.appium.java_client.android.AndroidDriver;
import io.appium.java_client.android.AndroidElement;

public class ExpandableLists extends Base {

	public static void main(String[] args) {

		AndroidDriver<AndroidElement> driver = capabilities();
		driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);
		driver.findElementByXPath("//android.widget.TextView[@text='Views']").click();
		driver.findElementByXPath("//android.widget.TextView[@text='Expandable Lists']").click();
		driver.findElementByXPath("//android.widget.TextView[@text='1. Custom Adapter']").click();
		driver.findElementByXPath("//android.widget.TextView[@text='People Names']").click();
		driver.findElementByXPath("//android.widget.TextView[@text='Adam']").click();
		driver.findElementByXPath("//android.widget.TextView[@text='
