import io.netty.handler.codec.http.HttpResponseStatus;
import io.netty.handler.codec.http.HttpVersion;

import java.util.Date;

import play.core.j.JavaResultExtractor;
import play.libs.F;
import play.libs.F.Promise;
import play.libs.Json;
import play.libs.ws.WS;
import play.libs.ws.WSResponse;
import play.libs.ws.ning.NingWSResponse;
import play.mvc.Http.Context;
import play.mvc.Result;
import play.mvc.Results;
import play.mvc.Results.Chunks;
import play.mvc.SimpleResult;

import com.ning.http.client.AsyncHttpClient;
import com.ning.http.client.Response;

/**
 * Implementation of the AsyncHttpClient API
 */
class NingWSImpl implements WS.WSImpl {

    private final AsyncHttpClient client;

    public NingWSImpl(AsyncHttpClient client) {
        this
