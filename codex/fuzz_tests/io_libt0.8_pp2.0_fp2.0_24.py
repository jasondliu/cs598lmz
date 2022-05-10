import io.restassured.response.Response;
import junit.framework.Assert;
import org.junit.AfterClass;
import org.junit.BeforeClass;
import org.junit.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class TestApi {

    private static Map<String, Object> jsonAsMap;
    private static List<Map<String, Object>> itemsList;

    @BeforeClass
    public static void beforeClass() {
        jsonAsMap = new HashMap<>();
        Response response = getMethod("/characters");
        jsonAsMap = response.as(HashMap.class);
        itemsList = (List<Map<String, Object>>) jsonAsMap.get("items");
    }

    @Test
    public void testStatusCode200() {
        Assert.assertEquals(200, getMethod("/characters").getStatusCode());
    }

    @Test
    public void testTotal() {
        Assert.
