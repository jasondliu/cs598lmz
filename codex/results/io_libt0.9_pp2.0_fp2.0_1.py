import io.undertow.security.api.SecurityContext;
import io.undertow.security.idm.Account;
import io.undertow.security.impl.SingleSignOnManager.AuthenticationResult;
import io.undertow.security.impl.SingleSignOnManager.SSOCredentialCallback;
import io.undertow.server.HttpServerExchange;
import io.undertow.util.FlexBase64;
import io.undertow.util.HeaderMap;
import io.undertow.util.HeaderValues;
import io.undertow.util.Headers;

/**
 * Negotiation authentication mechanism.
 *
 * This is intended to be used in conjunction with SSO, to allow a HTTP/1.1 request to be converted into a HTTP/1.0
 * request to work around intermediaries that do not support authentication headers on HTTP/1.1 requests.
 *
 * It is loosely based on the Apache mod_negotiation, but the implementation is different. For reference the
 * implementation used by Apache can be found here:
 *
 * http://svn.apache.org
