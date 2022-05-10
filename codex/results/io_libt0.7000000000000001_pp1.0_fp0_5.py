import io.restassured.specification.RequestSpecification;
import org.apache.http.HttpStatus;
import org.testng.annotations.Test;

import static org.hamcrest.Matchers.equalTo;
import static org.hamcrest.Matchers.instanceOf;
import static org.hamcrest.Matchers.not;

public class TestPost extends BaseTest {

    @Test
    public void postTest() {

        RequestSpecification request = RestAssured.given();
        JSONObject jsonObject = new JSONObject();
        jsonObject.put("name", "morpheus");
        jsonObject.put("job", "leader");

        request.body(jsonObject.toJSONString());

        Response response = request.post("/users");

        response.then().assertThat().contentType(ContentType.JSON)
                .and().statusCode(HttpStatus.SC_CREATED)
                .and().body("name", equalTo("morpheus"))
                .and().body("job", equalTo("leader"))
                .and().body("id", not(equalTo(null)))

