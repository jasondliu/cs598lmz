import io.*;
import scala.math.Ordering;

public class TestWordCount {
	
	public static void main(String[] args) throws Exception {
		
		SparkConf conf = new SparkConf().setMaster("local").setAppName("WordCount");
		JavaSparkContext sc = new JavaSparkContext(conf);
		
		// Load in the text file
		JavaRDD<String> textFile = sc.textFile("/home/ubuntu/spark/tweet.txt");
		
		// Java 8 with lambdas: split the input string into words
		
		JavaRDD<String> words = textFile.flatMap(s -> Arrays.asList(s.split(" ")).iterator());
		
		// Java 8 with lambdas: transform the collection of words into pairs (word and 1) and then count them
		JavaPairRDD<String, Integer> counts = words.mapToPair(w -> new Tuple2<String, Integer>(w, 1)).reduceByKey((x, y) ->
