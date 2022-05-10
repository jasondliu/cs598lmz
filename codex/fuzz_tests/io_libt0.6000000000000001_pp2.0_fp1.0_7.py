import io.reactivex.disposables.Disposable;
import io.reactivex.functions.Consumer;
import io.reactivex.internal.disposables.DisposableHelper;
import io.reactivex.internal.queue.SpscLinkedArrayQueue;
import io.reactivex.internal.util.AtomicThrowable;
import io.reactivex.plugins.RxJavaPlugins;

public final class FlowableOnBackpressureBuffer<T> extends AbstractFlowableWithUpstream<T, T> {
    final int bufferSize;
    final boolean delayError;
    final boolean unbounded;

    static final class BackpressureBufferSubscriber<T> extends AtomicInteger implements FlowableSubscriber<T>, Disposable {
        private static final long serialVersionUID = -2514538129242366402L;
        volatile boolean cancelled;
        volatile boolean done;
        final boolean delayError;
        Throwable error;
        final SpscLinkedArrayQueue<T> queue;
        final AtomicThrowable errorRef;
        final AtomicLong requested = new AtomicLong();
