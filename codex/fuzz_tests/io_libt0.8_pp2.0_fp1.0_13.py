import io.reactivex.Single
import io.sinq.repository.Repository
import io.sinq.provider.Page

class PageHelper[T, ID](val repository: Repository[T, ID], val page: Page[T, ID]) {

  def exists(id: ID): Single[Boolean] = {
    repository.exists(id)
  }

  def list(): Single[java.util.List[T]] = {
    repository.list(page)
  }

  def count(): Single[Long] = {
    repository.count()
  }

  def save(t: T): Single[Boolean] = {
    repository.save(t)
  }

  def update(t: T): Single[Boolean] = {
    repository.update(t)
  }

  def delete(t: T): Single[Boolean] = {
    repository.delete(t)
  }
}
