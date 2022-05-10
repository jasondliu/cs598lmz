import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.SignatureAlgorithm;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Component;

import java.util.Date;


/**
 * @author 刘佳兴
 */
@Component
@Slf4j
public class JwtUtil {

    public String generateToken(UserDetailsImpl userDetails) {
        String token = Jwts.builder()
                // 设置主题信息
                .setSubject(userDetails.getUsername())
                // 设置失效时间
                .setExpiration(new Date(System.currentTimeMillis() + JwtConfig.TOKEN_EXPIRE_TIME))
                // 设置签发时间
                .setIssuedAt(new Date())
                // 设置签名算法和密
