import io.github.jhipster.web.util.ResponseUtil;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.ResponseEntity;
import org.springframework.transaction.annotation.Transactional;
import org.springframework.web.bind.annotation.*;

import java.net.URI;
import java.net.URISyntaxException;
import java.util.List;
import java.util.Optional;

/**
 * REST controller for managing {@link it.epocaricerca.geologia.model.Danno}.
 */
@RestController
@RequestMapping("/api")
@Transactional
public class DannoResource {

    private final Logger log = LoggerFactory.getLogger(DannoResource.class);

    private static final String ENTITY_NAME = "danno";

    @Value("${jhipster.clientApp.name}")
    private
