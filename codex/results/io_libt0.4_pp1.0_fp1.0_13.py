import io.reactivex.Single
import io.reactivex.schedulers.Schedulers
import javax.inject.Inject

class GetTasksUseCase @Inject constructor(
    private val tasksRepository: TasksRepository
) {

    fun execute(): Single<List<Task>> {
        return tasksRepository.getTasks()
            .subscribeOn(Schedulers.io())
    }
}
