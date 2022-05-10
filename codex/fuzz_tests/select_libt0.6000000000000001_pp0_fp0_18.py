import selector from '../../../../../state/Selector';
import {connect} from 'react-redux';
import appResources from '../../../../../appResources';
import {NavigationActions} from 'react-navigation';
import {resetFilters} from '../../../../../state/Actions';

class ResetFiltersButton extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      resetFiltersButton: null,
    };
  }

  componentDidMount() {
    this.setResetFiltersButton();
  }

  setResetFiltersButton() {
    const resetFiltersButton =
      this.props.filters.length > 0 ? (
        <TouchableOpacity
          onPress={() => {
            this.props.resetFilters();
            this.props.navigation.dispatch(
              NavigationActions.navigate({
                routeName: 'FilterScreen',
              }),
            );
          }}>
          <Image
            style={{
              width
