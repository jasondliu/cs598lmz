import selectExpensesTotal from '../selectors/expenses-total';


export const ExpensesSummary = ({ total, expenseCount }) => {
  return (
  <div>
    <h1>Viewing {expenseCount} expenses totalling ${total}</h1>
  </div>
)};


const mapStateToProps = (state) => {
  const visibleExpenses = selectExpenses(state.expenses, state.filters);
  return {
    expenseCount: visibleExpenses.length,
    total: numeral(selectExpensesTotal(visibleExpenses) / 100).format('$0,0.00')
  }
};

export default connect(mapStateToProps)(ExpensesSummary);
