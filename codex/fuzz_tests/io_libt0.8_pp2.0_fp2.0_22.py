import io.fabric.sdk.android.services.concurrency.internal.RetryState;
import io.fabric.sdk.android.services.concurrency.internal.SimpleRetryPolicy;
import io.fabric.sdk.android.services.concurrency.internal.SystemCurrentTimeProvider;
import io.fabric.sdk.android.services.concurrency.internal.TaskImpl;
import io.fabric.sdk.android.services.concurrency.internal.TaskQueue;
import io.fabric.sdk.android.services.concurrency.internal.TaskRunnerImpl;
import io.fabric.sdk.android.services.concurrency.internal.Worker;
import io.fabric.sdk.android.services.concurrency.internal.Worker.WorkerListener;
import java.util.Collections;
import java.util.HashSet;
import java.util.List;
import java.util.concurrent.atomic.AtomicBoolean;
import java.util.concurrent.atomic.AtomicReference;

public class PriorityAsyncTask extends AsyncTask<Void,
