import selectedTimelines from '../../selectors/timeline';
import { connect } from 'react-redux';
import { Link } from 'react-router-dom';

export class TimelineList extends React.Component {
  render() {
    return (
      <div className="content-container">
      <div className="list-header">
        <div className="show-for-mobile">Timelines</div>
        <div className="show-for-desktop">Timeline</div>
      </div>
      <div className="list-body">
      {
        this.props.timelines.length === 0 ? (
          <div className="list-item list-item__message">
            <p>No timelines</p>
          </div>
        ) : (
          this.props.timelines.map((timeline) => {
          return <TimelineListItem key={timeline.id} {...timeline} />;
         })
        )
      }
    </div>
    <div className="page-header__actions">
      <
