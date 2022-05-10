import selectExpenses from '../selectors/expenses';
import selectExpensesTotal from '../selectors/expenses-total';

export const ExpenseSummary = ({ expenseCount, expenseTotal}) => {
  const word = expenseCount === 1 ? "expense" : "expenses";
  const amount = numeral(expenseTotal/100).format('$0,0.00');
  return (
    <div>
      <h1>Viewing {expenseCount} {word} totalling {amount}</h1>
    </div>
  );
};

//Connecting to Redux
const mapStateToProps = (state) => {
  const visibleExpenses = selectExpenses(state.expenses, state.filters);
  return {
    expenseCount: visibleExpenses.length,
    expenseTotal: selectExpensesTotal(visibleExpenses)
  };
};

export default connect(mapStateToProps)(ExpenseSummary);
