import io.reactivex.functions.Function;
import io.reactivex.functions.Predicate;
import io.reactivex.processors.PublishProcessor;
import io.reactivex.schedulers.Schedulers;
import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.TimeUnit;

public final class MainActivity extends AppCompatActivity implements
    RxPermissions.OnRequestPermissionsResultCallback {

  private static final int REQUEST_CAMERA = 101;
  private static final int REQUEST_AUDIO = 102;
  private static final int REQUEST_STORAGE = 103;
  private static final int REQUEST_CONTACTS = 104;

  private static final int REQUEST_CAMERA_AND_STORAGE = 105;
  private static final int REQUEST_AUDIO_AND_STORAGE = 106;
  private static final int REQUEST_CONTACTS_AND_STORAGE = 107;

  private static final int REQUEST_CAMERA_AND_AUDIO = 108;

 
