import io.crate.protocols.postgres.types.PGType;
import io.crate.sql.tree.DereferenceExpression;
import io.crate.sql.tree.Expression;
import io.crate.sql.tree.QualifiedName;
import io.crate.expression.operator.AnyOperator;
import io.crate.expression.operator.Operator;
import io.crate.expression.operator.Operators;
import io.crate.expression.operator.SubscriptArrayOperator;
import io.crate.expression.operator.SubscriptObjectOperator;
import io.crate.expression.scalar.AbstractScalarFunctionsTest;
import io.crate.expression.scalar.ScalarFunctionModule;
import io.crate.expression.symbol.Function;
import io.crate.expression.symbol.Symbol;
import io.crate.expression.symbol.SymbolType;
import io.crate.expression.symbol.fucnctions.ScalarFunction;
import io.crate.expression.
