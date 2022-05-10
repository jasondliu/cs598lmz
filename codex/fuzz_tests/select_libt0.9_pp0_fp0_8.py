import selectExpenses from '../selectors/expenses';
import expensesTotal from '../selectors/expenses-total';

export const ExpensesSummary = ({expensesCount, expensesTotalSum}) => {
    const expenseWord = expensesCount === 1 ? 'expense' : 'expenses';
    const formatedTotalSum = numeral(expensesTotalSum/100).format('$0,0.00');
    return (
        <div>
            <p>Viewing {expensesCount} {expenseWord} totalling {formatedTotalSum}</p>
        </div>
    );
};

const mapStateToProps = (state) => {
    const visibleExpenses = selectExpenses(state.expenses, state.filters);
    return {
        expensesCount: visibleExpenses.length,
        expensesTotalSum: expensesTotal(visibleExpenses)
    }
}

export default connect(mapStateToProps)(ExpensesSummary);
