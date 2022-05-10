import io.restassured.response.Response;
import io.restassured.response.ValidatableResponse;
import io.restassured.specification.RequestSpecification;

public class BaseClass {


	public static Response response;
	@BeforeMethod
	public void setUp() {
		RestAssured.baseURI = "https://dev99630.service-now.com/api/now/v2/table/";
		RestAssured.authentication = RestAssured.basic("admin", "q3g1iQKmtMkS");
	}

	public static ValidatableResponse getResponseBody() {

		RequestSpecification request = RestAssured.given();
		request.contentType(ContentType.JSON);

		// Get the response
		response = request.get("incident");

		// Return the response body
		return response.then();

	}

	public static ValidatableResponse createIncident(JsonObject json) {

		RequestSpecification request = RestAssured.given();
		request.contentType(ContentType.JSON);


