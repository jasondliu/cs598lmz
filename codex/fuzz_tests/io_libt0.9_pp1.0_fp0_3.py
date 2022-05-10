import io.vertx.core.json.JsonObject;
import lombok.extern.slf4j.Slf4j;

@Slf4j
public class EmploymentInquiryServiceCommandHandler extends AbstractEISCommandHandler {
	
	public EmploymentInquiryServiceCommandHandler() {
		super(Command.class);
	}

	@Override
	public void execute(Vertx vertx, String clientId, String sessionId, long contextId, ICommand command)
			throws Exception {
		JsonObject jsonObject = encode(command);
		
		CommandProcessor.process(this.getClass().getSimpleName(), jsonObject, command);
	}

}
