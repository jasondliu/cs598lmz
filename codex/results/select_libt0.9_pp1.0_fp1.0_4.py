import selectExpenses from "../selectors/expenses";
import { addExpense, editExpense, setExpenses, removeExpense } from "../actions/expenses";
import { connect } from "react-redux";
import moment from "moment";

export class ExpensesList extends React.Component {
  onLoadMore = e => {
    const { loadExpenses } = this.props;
    loadExpenses();
  }

  render() {
    const { expenses, total, limit, count } = this.props;

    return (
      <div>
        <List
          className="expenses-list"
          header={<div className="expenses-list__header">Total: {total}</div>}
          bordered
          dataSource={expenses}
          renderItem={expense => (
            <List.Item>
              <List.Item.Meta
                title={expense.title}
                description={moment(expense.createdAt).format("MMMM Do, YYYY")}
              />{" "}
              {expense.amount
