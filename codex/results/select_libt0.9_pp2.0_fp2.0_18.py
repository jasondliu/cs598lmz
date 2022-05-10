import selector from '../selectors/employees';
import { connect } from 'react-redux';
import { fetchEmployees } from '../actions/employees';
import EmployeeListItem from './EmployeeListItem';
export class EmployeeList extends React.Component {
  componentDidMount() {
    this.props.fetchEmployees();
  }

  render() {
    return (
      <div className="content-container">
        <div className="list-header">
          <div className="show-for-mobile">Employees</div>
          <div className="show-for-desktop">Employee</div>
          <div className="show-for-desktop">Email</div>
        </div>
        <div className="list-body">
          {
            this.props.employees.length === 0 ? (
              <div className="list-item list-item--message">
                <span>No employees</span>
              </div>
            ) : (
                this.props.employees.map((employee) => {
                  return
