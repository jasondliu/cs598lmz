import io.cucumber.java.en.Then;

public class AnalyseReviewTest {

WebDriver driver;
	
	@Given("the user is on the application homepage")
	public void the_user_is_on_the_application_homepage() {
		System.setProperty("webdriver.chrome.driver", "C:\\Users\\A652292\\eclipse-workspace\\CucumberPOMFramework\\drivers\\chromedriver.exe");
		driver = new ChromeDriver(); 
		driver.manage().window().maximize(); 
		driver.manage().timeouts().implicitlyWait(5, TimeUnit.SECONDS);
		driver.get("https://example.testproject.io/web/");
	}

	@When("the user fills login name {string}")
	public void the_user_fills_login_name(String string) {
		LoginPage l = new LoginPage(driver);
		l.loginName().sendKeys(string);
	}

	@When("the user fills password {string}")
