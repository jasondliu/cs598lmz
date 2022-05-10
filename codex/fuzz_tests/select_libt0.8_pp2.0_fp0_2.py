import selectExpensesTotal from '../selectors/expenses-total';
import numeral from 'numeral';

const ExpensesSummary = (props) => {
    const expenseWord = props.expenseCount === 1 ? 'expense' : 'expenses' ;
    const formattedExpensesTotal = numeral(selectExpensesTotal(props.expenses) / 100).format('$0,0.00') ;
    return (
        <div>
            {
                props.expenseCount > 0 && (
                    <h1>Viewing {props.expenseCount} {expenseWord} totalling {formattedExpensesTotal}</h1>
                )
            }
        </div>
    )
}

const mapStateToProps = (state) => {
    return {
        expenseCount: state.expenses.length,
        expenses: state.expenses
    };
};

export default connect(mapStateToProps)(ExpensesSummary);
