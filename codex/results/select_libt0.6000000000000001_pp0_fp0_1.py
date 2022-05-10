import selectors from '../../selectors';

class ExpensesSummary extends Component {
  render() {
    const expensesCount = this.props.expenses.length;
    const expensesTotal = this.props.expenses.reduce((acc, curr) => {
      return acc + curr.amount;
    }, 0);
    const expenseWord = expensesCount === 1 ? 'expense' : 'expenses';
    return (
      <div>
        <h1>
          Viewing {expensesCount} {expenseWord} totalling{' '}
          {numeral(expensesTotal / 100).format('$0,0.00')}
        </h1>
      </div>
    );
  }
}

const mapStateToProps = state => ({
  expenses: selectors.getVisibleExpenses(state.expenses, state.filters)
});

export default connect(mapStateToProps)(ExpensesSummary);
