import io.restassured.mapper.ObjectMapper;
import io.restassured.mapper.ObjectMapperDeserializationContext;
import io.restassured.mapper.ObjectMapperSerializationContext;
import io.restassured.response.Response;
import io.restassured.specification.RequestSpecification;

public class Base {
	
	public static RequestSpecification httpRequest;
	public static Response response;
	public String empID=""; //Global Variable
	
	public Logger logger;
	
	@BeforeSuite
	public void setUp() {
		
		logger = LogManager.getLogger(Base.class);
		
		RestAssured.baseURI = "http://dummy.restapiexample.com/api/v1";
		RestAssured.basePath = "/";
		
		httpRequest = RestAssured.given();
		
		//Adding customer log
		//RestAssured.filters(new RequestLoggingFilter());
		
		//Adding customer deser
