import io.reactivex.Flowable;
import io.reactivex.Maybe;
import io.reactivex.Observable;
import io.reactivex.Single;
import retrofit2.http.Body;
import retrofit2.http.GET;
import retrofit2.http.POST;
import retrofit2.http.Path;
import retrofit2.http.Query;
import hr.cc.util.cassandra.cassandratester.telemetry.model.client.TelemetryClient;
import hr.cc.util.cassandra.cassandratester.telemetry.model.partitionkey.PartitionKey;
import hr.cc.util.cassandra.cassandratester.telemetry.model.resource.ResourceData;
import hr.cc.util.cassandra.cassandratester.telemetry.model.table.TelemetryTableV1;
import hr.cc.util.cassandra.cassandratester.telemetry.model.table.TelemetryTableV2;

/**
 * Created by Nemanja on 01.11.
