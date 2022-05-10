import selectTotalCount from "../selectors/selectTotalCount";
import selectIsFetching from "../selectors/selectIsFetching";
import { connect } from "react-redux";
import * as actions from "../actions";

class PeopleListContainerWithoutMemo extends React.Component {
  componentDidMount() {
    this.fetchData();
  }

  fetchData = () => {
    const { page, perPage } = this.props;

    this.props.fetchPeople(page, perPage);
  };

  findPersonByPersonId = personId => {
    const personResults = this.props.peopleResults.filter(
      result => result.personId === parseInt(personId, 10)
    );
    return personResults.length ? personResults[0] : null;
  };

  removeSelectedPerson = personId => {
    const person = this.findPersonByPersonId(personId);
    this.props.removeSelectedPerson(person);
  };

  render() {
    return (
      <PeopleList
        people
