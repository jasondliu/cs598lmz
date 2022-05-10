import io.cucumber.java.en.Given;
+import io.cucumber.java.en.Then;
+import io.cucumber.java.en.When;
+import io.github.bonigarcia.wdm.WebDriverManager;
+import pages.CreateOrderPage;
+import pages.LoginPage;
+import pages.PageBase;
+
+import static org.junit.jupiter.api.Assertions.assertEquals;
+
+public class TestSteps extends PageBase {
+    LoginPage loginPage;
+    CreateOrderPage createOrderPage;
+
+    @Before
+    public void beforeScenario() {
+        WebDriverManager.chromedriver().setup();
+        driver = new ChromeDriver();
+        loginPage = new LoginPage(driver);
+        createOrderPage = new CreateOrderPage(driver);
+    }
+
+    @After
+    public void afterScenario() {
+        driver.quit();
+    }
+
+    @Given("I login to application with username {string} and
