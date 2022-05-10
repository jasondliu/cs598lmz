import io.reactivex.Observable
import io.reactivex.Single
import io.reactivex.android.schedulers.AndroidSchedulers
import io.reactivex.schedulers.Schedulers
import io.realm.Realm
import io.realm.RealmResults
import io.realm.Sort
import javax.inject.Inject

class TasksRepository
@Inject constructor(
    private val tasksApi: TasksApi,
    private val realm: Realm
) {

    fun fetchTasks(): Single<List<Task>> {
        return tasksApi.getTasks()
    }

    fun fetchTasksSorted(sort: String): Observable<RealmResults<Task>> {
        return realm.where(Task::class.java)
            .sort(sort, Sort.DESCENDING)
            .findAllAsync()
            .asFlowable()
            .toObservable()
    }

    fun saveTasks(tasks: List<Task>) {
        realm.executeTransactionAsync { realm
