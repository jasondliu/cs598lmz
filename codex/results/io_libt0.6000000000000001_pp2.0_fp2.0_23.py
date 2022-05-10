import io.appium.java_client.AppiumDriver;
import io.appium.java_client.MobileElement;

public class LoginScreen {
	
	private AppiumDriver<MobileElement> driver;
	
	public LoginScreen(AppiumDriver<MobileElement> driver) {
		this.driver = driver;
	}
	
	public void setEmail(String email) {
		MobileElement element = driver.findElement(By.id("com.qltech.simpli.qa:id/et_email"));
		element.sendKeys(email);
	}
	
	public void setPassword(String password) {
		MobileElement element = driver.findElement(By.id("com.qltech.simpli.qa:id/et_password"));
		element.sendKeys(password);
	}
	
	public void clickLogin() {
		MobileElement element = driver.findElement(By.id("com.qltech.simpli.qa:id/btn_login"));
		element.click();
	}
	
	
