import io.jsonwebtoken.SignatureException;

public class TokenAuthenticationService {
	private static final String AUTH_HEADER_NAME = "X-AUTH-TOKEN";
	private static final long TEN_DAYS = 1000 * 60 * 60 * 24 * 10;
	private static final String SECRET = "roshan";
	private static final String EXPOSE_HEADER_NAME = "Access-Control-Expose-Headers";
	private static final String TOKEN_PREFIX = "Bearer";

	public static void addAuthentication(HttpServletResponse response, User user) {
		String JWT = Jwts.builder().setSubject(user.getUsername()).setExpiration(new Date(System.currentTimeMillis() + TEN_DAYS)).signWith(SignatureAlgorithm.HS512, SECRET).compact();
		response.addHeader(AUTH_HEADER_NAME, TOKEN_PREFIX + " " + JWT);
		response.addHeader(EXPOSE_HEADER_NAME, AUTH_HEADER_NAME);
	}

	
