import io.cucumber.junit.CucumberOptions;

@RunWith(Cucumber.class)
@CucumberOptions(features = "src/test/resources/features", plugin = { "pretty",
		"html:target/cucumber-reports" }, glue = "steps.login", tags = { "~@ignore" }, monochrome = true)
public class LoginRunnerTest {

}
