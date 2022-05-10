import io.appium.java_client.pagefactory.AppiumFieldDecorator;
import io.appium.java_client.pagefactory.iOSFindBy;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.support.PageFactory;

import java.util.concurrent.TimeUnit;


public class SearchScreen extends BaseScreen {

    //region CONSTRUCTOR
    public SearchScreen(WebDriver driver) {
        super(driver);
        PageFactory.initElements(new AppiumFieldDecorator(driver, Duration.ofSeconds(10)), this);
    }
    //endregion

    //region LOCATORS
    @iOSFindBy(xpath = "//XCUIElementTypeTextField[1]")
    private MobileElement textSearchField;

    @iOSFindBy(accessibility = "search")
    private MobileElement searchButton;
    //endregion

    //region METHODS
    public SearchScreen searchFor(String searchString) {
        sendKeys(textSearchField, searchString);
        return this;
    }
