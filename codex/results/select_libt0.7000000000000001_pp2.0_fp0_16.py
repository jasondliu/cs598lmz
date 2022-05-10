import selectexpense from '../selectors/expenses';
import selectexpensesTotal from '../selectors/expenses-total';
import numeral from 'numeral';

export const ExpensesSummary = ({expensesCount, expensesTotal}) => {
    const expenseWord = expensesCount === 1 ? 'expense' : 'expenses';
    const formattedExpensesTotal = numeral(expensesTotal/100).format('0,0.00');
    return (
        <div>
            <h2>Viewing {expensesCount} {expenseWord} totalling {formattedExpensesTotal}</h2>
        </div>
    );
};

const mapStateToProps = (state) => {
    const visableExpenses = selectexpense(state.expenses, state.filters);
    return {
        expensesCount: visableExpenses.length,
        expensesTotal: selectexpensesTotal(visableExpenses)
    };
};

export default connect(mapStateToProps)(ExpensesSummary);
