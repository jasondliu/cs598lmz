import io.farragoLang.farrago.parser.FarragoParser;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.CharStreams;
import org.antlr.v4.runtime.CommonTokenStream;
import org.antlr.v4.runtime.tree.ParseTree;

public class Driver {

    public static void main(String[] args) throws Exception {

        CharStream input = CharStreams.fromFileName(args[0]);
        FarragoLexer farragoLexer = new FarragoLexer(input);
        CommonTokenStream farragoTokens = new CommonTokenStream(farragoLexer);
        FarragoParser farragoParser = new FarragoParser(farragoTokens);
        ParseTree tree = farragoParser.program();
        FarragoVisitor farragoVisitor = new FarragoVisitImpl();
        farragoVisitor.visit(tree);


    }

}
