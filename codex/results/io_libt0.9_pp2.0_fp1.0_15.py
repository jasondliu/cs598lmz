import io.appium.java_client.android.AndroidDriver;
import io.appium.java_client.android.AndroidElement;

public class LinearLayout extends test {

    public static void main(String[] args) throws MalformedURLException {

        AndroidDriver<AndroidElement> driver = Capabilities();
        driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);

        driver.findElementByXPath("//android.widget.TextView[@text='Views']").click();
        driver.findElementByXPath("//android.widget.TextView[@text='Views']").click();

        //Scroll to some text that isn't visible on the screen
        driver.findElementByAndroidUIAutomator("new UiScrollable(new UiSelector()).scrollIntoView(text(\"WebView\"));");

        //click on webview
        driver.findElementByXPath("//android.widget.TextView[@text='WebView']").click();
        driver.findElementByXPath("//android.widget.TextView[
