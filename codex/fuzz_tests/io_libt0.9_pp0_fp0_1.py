import io.restassured.http.ContentType;
import io.restassured.response.ValidatableResponse;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Component;

@Component
@Slf4j
public class AuthenticationAPI {
  private final String BASE_URI;
  private final String BASE_PATH;

  public AuthenticationAPI(@Value("${baseURI}") String BASE_URI, @Value("${basePath}") String BASE_PATH) {
    this.BASE_URI = BASE_URI;
    this.BASE_PATH = BASE_PATH;
  }

  public String getJWT(String username, String password) {
    String token =
        given()
            .baseUri(BASE_URI)
            .basePath(BASE_PATH)
            .contentType(ContentType.JSON)
            .body(getNewUserBody(username, password))
            .when()
            .post("/token/en
