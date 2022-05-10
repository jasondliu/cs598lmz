import io.reactivex.Single;

/**
 * Created by 홍성호 on 2017-11-02.
 */

public class GetUserInfoUseCase extends SingleUseCase<UserInfo> {

    private final UserRepository userRepository;

    @Inject
    public GetUserInfoUseCase(UserRepository userRepository) {
        this.userRepository = userRepository;
    }

    @Override
    protected Single<UserInfo> buildUseCaseSingle(Params params) {
        return userRepository.getUserInfo();
    }
}
