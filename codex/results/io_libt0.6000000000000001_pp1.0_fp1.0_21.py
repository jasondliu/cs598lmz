import io.jsonwebtoken.ExpiredJwtException;
import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.MalformedJwtException;
import io.jsonwebtoken.SignatureAlgorithm;
import io.jsonwebtoken.SignatureException;
import io.jsonwebtoken.UnsupportedJwtException;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.security.core.Authentication;
import org.springframework.stereotype.Component;

import java.util.Date;
import java.util.Optional;

@Component
public class JwtProvider {

    private static final String USER_ID = "userId";

    private static final String USER_NAME = "userName";

    private static final String USER_ROLES = "userRoles";

    private final JwtSecret jwtSecret;

    @Value("${security.jwt.expiration.time}")
    private long jwtExpirationInMs;


