import io.restassured.http.Method;
import io.restassured.response.Response;
import io.restassured.specification.RequestSpecification;

public class Replace_keyword 
{

	public static void main(String[] args) 
	{
		//create object for restAssured class
		RestAssured.baseURI="https://restcountries.eu";
		
		//create object for RequestSpecification interface
		RequestSpecification httprequest= RestAssured.given();
		
		//create object for response interface
		Response response=httprequest.request(Method.GET,"/rest/v2/name/india");
		
		//Capture Response body to perform validation
		String responsebody=response.getBody().asString();
		System.out.println("Response body is:"+responsebody);
		
		//Capture status code
		int statuscode=response.getStatusCode();
		System.out.println("status code is:"+statuscode);
		
		//Capture status line

