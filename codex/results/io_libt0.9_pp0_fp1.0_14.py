import io.dropwizard.auth.UnauthorizedHandler;
import io.dropwizard.jersey.validation.Validators;

import java.util.List;

import javax.ws.rs.WebApplicationException;
import javax.ws.rs.container.ContainerRequestContext;
import javax.ws.rs.core.HttpHeaders;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;

import org.apache.commons.lang3.StringUtils;

import com.google.common.base.Optional;
import com.google.common.base.Preconditions;
import com.google.common.collect.Lists;

/**
 * Handler for unauthorized responses to given security scheme
 *
 * @param <T>
 */
public class SchemeUnauthorizedHandler<T> implements UnauthorizedHandler {

    private final String serverSideAuthenticationScheme;

    /**
     * UnauthorizedHandler for given security scheme
     *
     * @param securitySchemeName
     */
   
