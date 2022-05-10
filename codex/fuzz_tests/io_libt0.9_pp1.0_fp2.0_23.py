import io.github.jhipster.web.util.ResponseUtil;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import javax.validation.Valid;
import java.net.URI;
import java.net.URISyntaxException;

import java.util.List;
import java.util.Optional;

/**
 * REST controller for managing Immobilisation.
 */
@RestController
@RequestMapping("/api")
public class ImmobilisationResource {

    private final Logger log = LoggerFactory.getLogger(ImmobilisationResource.class);

    private static final String ENTITY_NAME = "immobilisation";

    private final ImmobilisationRepository immobilisationRepository;

    public ImmobilisationResource(ImmobilisationRepository immobilisationRepository) {
        this.immobilisationRepository = immobilisationRepository;
    }

    /**
     * POST  /immobilisations :
