import io.github.jhipster.service.filter.StringFilter;
import io.github.jhipster.service.filter.LongFilter;

/**
 * Criteria class for the {@link com.mycompany.myapp.domain.EntityWithServiceClassAndPagination} entity. This class is used
 * in {@link com.mycompany.myapp.web.rest.EntityWithServiceClassAndPaginationResource} to receive all the possible filtering options from
 * the Http GET request parameters.
 * For example the following could be a valid request:
 * {@code /entity-with-service-class-and-paginations?id.greaterThan=5&attr1.contains=something&attr2.specified=false}
 * As Spring is unable to properly convert the types, unless specific {@link Filter} class are used, we need to use
 * fix type specific filters.
 */
public class EntityWithServiceClassAndPaginationCriteria implements Serializable, Criteria {

    private static final long serialVersionUID = 1L;

    private LongFilter id;

    private StringFilter theo;


