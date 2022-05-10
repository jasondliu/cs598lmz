import io.reactivex.schedulers.Schedulers;
import io.reactivex.subjects.PublishSubject;
import io.reactivex.subjects.Subject;
import retrofit2.Response;

/**
 * Created by mike on 2019-08-21.
 */
public class ProjectDetailsPresenter {

    private final String TAG = ProjectDetailsPresenter.class.getSimpleName();
    private Subject<ProjectDetailsEditingAction> actions;

    private ProjectDetailsView view;
    private ProjectDetailsEditingViewState viewState;
    private ProjectsRepository projectsRepository;
    private Resources resources;

    public ProjectDetailsPresenter(Context context, Resources resources,
                                   ProjectDetailsView view, ProjectsRepository projectsRepository) {
        this.view = view;
        this.projectsRepository = projectsRepository;
        this.resources = resources;
        initViewState();
        initActionSubject();
    }

    private void initViewState() {
        viewState = new ProjectDetailsEditingViewState();
    }

    private void initActionSubject() {
        actions =
