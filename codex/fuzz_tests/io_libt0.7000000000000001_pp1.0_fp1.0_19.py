import io.netty.handler.timeout.IdleStateEvent;
import io.netty.handler.timeout.IdleStateHandler;
import io.netty.util.concurrent.DefaultEventExecutorGroup;
import io.netty.util.concurrent.EventExecutorGroup;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.context.properties.EnableConfigurationProperties;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import java.util.concurrent.TimeUnit;

/**
 * @Description:
 * @Author: zhangss
 * @Date: 2020/5/28 23:57
 */
@Configuration
@EnableConfigurationProperties(NettyProperties.class)
public class NettyConfig {

    private static final Logger logger = LoggerFactory.getLogger(NettyConfig.class);

    @Autowired
    private
