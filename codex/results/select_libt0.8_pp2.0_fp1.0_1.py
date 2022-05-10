import selectRange from 'lib/event-utils/select-range';

const d = React.DOM;
const {_} = window._;

export default React.createClass({
  displayName: 'TimeAxis',

  propTypes: {
    times: React.PropTypes.array.isRequired,
    autoScroll: React.PropTypes.bool,
    width: React.PropTypes.number,
    getTimerange: React.PropTypes.func,
    setTimerange: React.PropTypes.func,
    tracks: React.PropTypes.array
  },

  getDefaultProps () {
    return {
      autoScroll: true,
      width: 0
    };
  },

  getInitialState () {
    return {
      range: null, // Range as [startTime, endTime]
      rangeTime: null,
      mousedown: false,
      selection: null
    };
  },

  getBrush () {
    const {width} = this.props;
    const {range} = this.state;

    let rangeDisplay = null;
   
