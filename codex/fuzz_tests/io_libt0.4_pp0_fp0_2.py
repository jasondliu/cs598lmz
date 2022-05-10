import io.restassured.RestAssured;
import io.restassured.http.ContentType;
import io.restassured.response.Response;
import io.restassured.specification.RequestSpecification;
import org.json.JSONObject;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;

import static io.restassured.RestAssured.given;
import static org.hamcrest.CoreMatchers.equalTo;

public class PostTest {

    @BeforeClass
    public void setUp() {
        RestAssured.baseURI = "https://api.github.com";
    }

    @Test
    public void createNewRepo() {
        RequestSpecification requestSpecification = given().contentType(ContentType.JSON)
                .auth().preemptive().basic("vladislav.korotkiy", "Vladislav1");
        JSONObject jsonObject = new JSONObject();
        jsonObject.put("name", "test");
        jsonObject.put("description", "test");
       
