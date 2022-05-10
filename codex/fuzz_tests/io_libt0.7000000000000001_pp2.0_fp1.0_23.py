import io.firebus.utils.DataMap;
import io.firebus.utils.DataTypes;

import java.util.Date;
import java.util.UUID;

public class TestService extends ServiceProvider
{
	protected TestService(ServiceContainer sc, String n)
	{
		super(sc, n);
		serviceName = n;
		sc.registerServiceProvider(this);
	}

	public void requestHandler(Request req, Response res)
	{
		try
		{
			DataMap reqBody = req.getBody().getObject("request");
			DataMap responseBody = new DataMap();
			
			if(reqBody.getString("method").equals("echo"))
			{
				responseBody.put("result", reqBody.getString("content"));
			}
			else if(reqBody.getString("method").equals("echoIn"))
			{
				int count = reqBody.getNumber("count").intValue();
		
