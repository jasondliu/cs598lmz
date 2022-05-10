import selectedFlights from '../selectors/flights';
import selectFlightsTotal from '../selectors/flights-total';

export const FlightSummary = ({ flightCount, flightsTotal }) => {
  const flightWord = flightCount === 1 ? 'flight' : 'flights';
  const formattedFlightsTotal = numeral(flightsTotal / 100).format('$0,0.00');
  
  return (
    <div className="page-header">
      <div className="content-container">
        <h1 className="page-header__title">Viewing <span>{flightCount}</span> {flightWord} totalling <span>{formattedFlightsTotal}</span></h1>
        <div className="page-header__actions">
          <Link className="button" to="/create">Add Flight</Link>
        </div>
      </div>
    </div>
  );
};

const mapStateToProps = (state) => {
  const visibleFlights = selectedFlights(state.flights, state.filters);

  return {
