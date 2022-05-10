import io.swagger.jaxrs.ext.multipart.Attachment;
import io.swagger.jaxrs.ext.multipart.Multipart;

import javax.servlet.ServletConfig;
import javax.ws.rs.Consumes;
import javax.ws.rs.GET;
import javax.ws.rs.POST;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.Response;
import javax.ws.rs.core.SecurityContext;
import javax.ws.rs.core.UriInfo;

@Path("/upload")

@Api(description = "the upload API")

public class UploadApi  {
   private final UploadApiService delegate = UploadApiServiceFactory.getUploadApi();

    @POST
    @Path("/json")
    @Consumes({ "application/json" })
    @Produces({ "
