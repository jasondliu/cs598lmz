import selectExpenses from '../selectors/expenses'
import { getVisibleExpenses } from '../selectors/expenses'

export class ExpenseList extends React.Component {

  render() {
    return (
      <div>
      <h1>Expense List</h1>
      {this.props.expenses.map((expense) => {
        return <ExpenseListItem key={expense.id} {...expense} />
      })}
      </div>
    )
  }
}

// const ConnectedExpenseList = connect((state) => {
//   return {
//     expenses: state.expenses
//   }
// })(ExpenseList)

const ConnectedExpenseList = connect((state) => {
  return {
    expenses: getVisibleExpenses(state.expenses, state.filters)
  }
})(ExpenseList)

export default ConnectedExpenseList
