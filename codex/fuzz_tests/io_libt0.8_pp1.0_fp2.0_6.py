import io.github.ovso.massage.framework.adapter.BaseAdapterDataModel
import io.github.ovso.massage.framework.listener.EndlessRecyclerOnScrollListener
import io.github.ovso.massage.framework.utils.RxBus
import io.github.ovso.massage.framework.utils.ViewUtils
import io.github.ovso.massage.main.f_acupoints.model.IAcupointsDataModel
import io.github.ovso.massage.main.f_acupoints.model.IAcupointsNetworkRepository
import io.github.ovso.massage.main.f_acupoints.model.IAcupointsViewModel
import io.github.ovso.massage.main.f_acupoints.model.dto.Acupoints
import io.github.ovso.massage.utils.rx.SchedulersFacade
import javax.inject.Inject
import javax.inject.Named

class AcupointsDataModel @Inject
