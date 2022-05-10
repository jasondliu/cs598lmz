import io.reactivex.Observable;

public class EntityConverter {

    private EntityConverter() {
    }

    public static Observable<List<Entity>> convertToEntityList(Observable<List<ApiEntity>> apiEntityList) {
        return apiEntityList.flatMapIterable(apiEntities -> apiEntities)
                .flatMap(apiEntity -> Observable.just(new Entity(apiEntity.getId(), apiEntity.getName())))
                .toList().toObservable();
    }
}
