import io.swagger.models.parameters.Parameter;
import io.swagger.models.Swagger;
import io.swagger.models.properties.Property;

import javax.ws.rs.*;
import javax.ws.rs.core.Response;
import java.util.List;
import java.util.Map;

@Path("/Confluence")
public interface ConfluenceResourceApi  {

    @GET
    @Path("/attachment")
    @Produces({ "application/json" })
    @ApiOperation(value = "", notes = "Gets all the attachments of a Confluence page", response = ConfluencePageAttachmentDTO.class, responseContainer = "List", authorizations = {
        @Authorization(value = "Basic")
    }, tags={ "Confluence",  })
    @ApiResponses(value = { 
        @ApiResponse(code = 200, message = "Operation successful", response = ConfluencePageAttachmentDTO.class, responseContainer = "List"),
        @ApiResponse(code = 400, message = "Invalid request
