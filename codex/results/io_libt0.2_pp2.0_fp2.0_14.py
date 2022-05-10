import io.github.jhipster.service.filter.BooleanFilter;
import io.github.jhipster.service.filter.DoubleFilter;
import io.github.jhipster.service.filter.Filter;
import io.github.jhipster.service.filter.FloatFilter;
import io.github.jhipster.service.filter.IntegerFilter;
import io.github.jhipster.service.filter.LongFilter;
import io.github.jhipster.service.filter.StringFilter;

/**
 * Criteria class for the {@link com.mycompany.myapp.domain.EntityWithServiceClassAndPagination} entity. This class is used
 * in {@link com.mycompany.myapp.web.rest.EntityWithServiceClassAndPaginationResource} to receive all the possible filtering options from
 * the Http GET request parameters.
 * For example the following could be a valid request:
 * {@code /entity-with-service-class-and-paginations?id.greaterThan=5&attr1.contains=something&attr2.specified=false}
