import io.appium.java_client.pagefactory.AndroidFindBy;
import io.appium.java_client.pagefactory.AppiumFieldDecorator;
import io.appium.java_client.pagefactory.iOSXCUITFindBy;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.PageFactory;

public class LoginPage {

    public LoginPage(WebDriver driver){
        PageFactory.initElements(new AppiumFieldDecorator(driver), this);
    }

    @AndroidFindBy(id = "com.code2lead.kwad:id/editTextEmail")
    @iOSXCUITFindBy(xpath = "//XCUIElementTypeTextField[@value='email@gmail.com']")
    public WebElement email;

    @AndroidFindBy(id = "com.code2lead.kwad:id/editTextPassword")
    @iOSXCUITFindBy(xpath = "//XCUIElementTypeSecureTextField
