import io.restassured.RestAssured;
import io.restassured.http.ContentType;
import java.util.HashMap;
import static org.hamcrest.Matchers.equalTo;
import static org.hamcrest.Matchers.hasSize;
import org.junit.Before;
import org.junit.Test;

public class IntegrationTest {

    static final String TEST_SERVER_URL = "http://localhost:8080";
    static final String APPLICATION_PATH = "/movie_rating";

    @Before
    public void setUp() {
        RestAssured.baseURI = TEST_SERVER_URL;
        RestAssured.basePath = APPLICATION_PATH;
        RestAssured.enableLoggingOfRequestAndResponseIfValidationFails();
    }

    /**
     * Test of addRating method, of class MovieRatingResource.
     */
    @Test
    public void testAddRating() {
        System.out.println("addRating");
        int userID = 1;
        int movieID = 1;
        int rating = 4;
       
