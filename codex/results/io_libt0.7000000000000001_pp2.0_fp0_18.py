import io.reactivex.observers.TestObserver;
import retrofit2.Response;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertNotNull;
import static org.mockito.Mockito.when;

@RunWith(MockitoJUnitRunner.class)
public class ApiTest {

    @Mock
    private ApiService apiService;
    private Api api;

    @Before
    public void setUp() {
        api = new Api(apiService);
    }

    @Test
    public void testFetchUsers() {
        when(apiService.fetchUsers()).thenReturn(Observable.just(Response.success(MockResponses.mockUsersResponse())));

        TestObserver<Response<UsersResponse>> testObserver = api.fetchUsers().test();
        testObserver.assertNoErrors();
        testObserver.assertValueCount(1);
        testObserver.assertComplete();

        Response<UsersResponse> response = testObserver
