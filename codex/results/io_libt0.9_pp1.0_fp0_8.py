import io.restassured.response.Response;

public class JiraTestController {
	
	private static String TOKEN=""; 
	private static String TEMP="";
	
	
	String url= "https://jira.hillel.it/rest/api/2/issue/QAAUT-25";
	
	
	public void loginToJira() {
	Response response= given().auth().preemptive().basic("kdaisy", "password").when().get("https://jira.hillel.it/rest/auth/1/session");

		TOKEN="Bearer "+response.then().extract().path("session.value");
		
	}
	
	public void createIssue() {
		
		
		@SuppressWarnings("unchecked")

		Response response = RestAssured.given().header("Content-Type", "application/json")
				.header("Authorization", TOKEN)
				.body("{\n" + 
						"  \"fields\": {\n"
