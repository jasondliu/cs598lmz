import io.shenanigans.concurrent.SingleListenerPromise;

/**
 *
 * @author whosea
 */
public class PythonContext extends org.spf4j.base.ExecutionContexts.ContextObject {

  public final SingleListenerPromise<PythonInterpreter> jsContextFut;

  public PythonContext(SingleListenerPromise<PythonInterpreter> jsContextFut) {
    this.jsContextFut = jsContextFut;
  }


}
