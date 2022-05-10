import io.vrap.rmf.raml.model.modules.Api;
import io.vrap.rmf.raml.model.security.SecurityScheme;

import java.util.Optional;

public class SecuritySchemeImpl extends ResourceBase implements SecurityScheme {

    public SecuritySchemeImpl(final RamlWrapper raml, final Api api) {
        super(raml, api);
    }

    @Override
    public Optional<String> getDescription() {
        return Optional.ofNullable(raml.getString("description"));
    }

    @Override
    public void setDescription(final String description) {
        raml.set("description", description);
    }

    @Override
    public Optional<String> getType() {
        return Optional.ofNullable(raml.getString("type"));
    }

    @Override
    public void setType(final String type) {
        raml.set("type", type);
    }

    @Override
    public Optional<String> getName() {
        return Optional.ofNullable(raml
