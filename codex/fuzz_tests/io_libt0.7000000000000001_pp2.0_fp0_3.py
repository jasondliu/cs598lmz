import io.reactivex.Observable

@Module
class RemoteModule {

    @Provides
    @ApplicationScope
    fun provideRemoteService(retrofit: Retrofit): RemoteService {
        return retrofit.create(RemoteService::class.java)
    }

    @Provides
    @ApplicationScope
    fun provideRemoteServiceHelper(remoteService: RemoteService): RemoteServiceHelper {
        return RemoteServiceHelper(remoteService)
    }

    @Provides
    @ApplicationScope
    fun provideRepository(remoteServiceHelper: RemoteServiceHelper): Repository {
        return Repository(remoteServiceHelper)
    }

    @Provides
    @ApplicationScope
    fun provideRemoteDataSource(repository: Repository): RemoteDataSource {
        return RemoteDataSource(repository)
    }

    @Provides
    @ApplicationScope
    fun providesRemoteDataSourceMapper(): RemoteDataSourceMapper {
        return RemoteDataSourceMapper()
    }

    @Provides
    @ApplicationScope
    fun providesRemoteDataSourcePort(remoteDataSource: RemoteDataSource): RemoteDataSource
