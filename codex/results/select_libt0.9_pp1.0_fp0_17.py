import selectjava.*;
import selectjava.Parser;
import selectjava.Compiler;
import selectjava.Env;

/**
 * This class runs the select compiler and 
 * outputs either the java implementation of the
 * select statement or the output of the select
 * statement itself.
 */
public class InvokeSelect {
  final static String version = "0.2";
  static boolean compiled = false;
  static boolean debug = false;
  static String classname = "Select";
  static String output_file = null;
  static String input_file = null;

  static String bootclasspath = null;
  static String classpath = null;

  static void usage() {
    printVersion();
    System.out.println("Usage: java selectjava.InvokeSelect" +
		       " (options) <select statement>");
    System.out.println("	-c	generate class file only");
    System.out.println("	-v	print compiler version");
    System.out.println("	-d	debug");
    System.out.println("	-o out	output
