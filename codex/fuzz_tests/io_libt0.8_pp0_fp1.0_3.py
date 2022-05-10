import io.micronaut.http.annotation.Param;
import io.reactivex.Single;

import java.util.List;

/**
 * API for working with containers from a container runtime (e.g. docker)
 *
 * @author James Kleeh
 * @since 1.0.0
 */
@Controller("/containers")
public interface ContainerOperations {

    /**
     * List all containers.
     *
     * @param quiet   Only return numeric IDs
     * @param size    Show the containers sizes
     * @param all     Show all containers (default shows just running)
     * @param limit   Limit the number of containers returned
     * @param filters A json encoded value of the filters (a map[string][]string) to process on the containers list. Available filters:
     *                - since (container's created time)
     *                - before (container's created time)
     *                - label (label=<key> or label=<key>=<value>)
     *                - exited (int)
     *                - status (created, restarting, running, removing,
