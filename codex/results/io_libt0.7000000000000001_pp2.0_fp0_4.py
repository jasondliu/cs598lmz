import io.github.zwieback.familyfinance.core.activity.Activity
import io.github.zwieback.familyfinance.core.activity.filter.EntityActivityFilter
import io.github.zwieback.familyfinance.core.model.IBaseEntity

abstract class BaseEntityActivity<E : IBaseEntity> : Activity() {

    protected abstract val filter: EntityActivityFilter<E>
}
