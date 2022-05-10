import io.yawp.repository.query.QueryBuilder;
import io.yawp.servlet.ChildEndpointServlet;
import io.yawp.servlet.EndpointServlet;
import io.yawp.servlet.ParentEndpointServlet;
import io.yawp.servlet.QueryServlet;
import io.yawp.servlet.SimpleEndpointServlet;
import io.yawp.servlet.YawpServlet;
import io.yawp.tools.cli.YawpCli;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public abstract class YawpServletsModule extends ServletsModule {

    public YawpServletsModule() {
    }

    @Override
    public void configure() {
        super.configure();

        bind(ObjectMapper.class).toProvider(ObjectMapperProvider.class).in(Singleton.class);
        bind(Yawp.class).toProvider(Y
