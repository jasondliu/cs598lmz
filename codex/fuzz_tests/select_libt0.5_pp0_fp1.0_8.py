import selector from './selector';
import {createSelector} from 'reselect';

const mapStateToProps = createSelector(
  selector,
  (state) => ({
    isLoading: state.isLoading,
    error: state.error,
    data: state.data
  })
);

export default connect(mapStateToProps, null)(Article);
