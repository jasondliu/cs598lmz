import io.reactivex.rxjava3.functions.Consumer;
import io.reactivex.rxjava3.functions.Function;
import io.reactivex.rxjava3.functions.Predicate;
import lombok.extern.slf4j.Slf4j;

@Slf4j
public class RxJava3Example {

	public static void main(String[] args) {

		// just 로 변환
		Observable<String> source = Observable.just("1", "2", "3");

		source.subscribe(data -> log.debug("OBSERVER #1 : {}", data));
		source.subscribe(data -> log.debug("OBSERVER #2 : {}", data));

		log.debug("-------------------------------------------------------------------");
		
		// map 으로 변환
		Observable<Integer> source2 = Observable.just("1", "2", "3").map(new Function<String, Integer>() {
			@Override
