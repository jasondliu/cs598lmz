import selectorVisibleTab from 'redux/reducers/selectorVisibleTab/selectorVisibleTab';

const mapStateToProps = (state) => {
  return {
    state: state,
    selectedTab: selectorVisibleTab(state)
  };
}

const mapDispatchToProps = (dispatch) => {
  return bindActionCreators({
    activeTab,
    handleSearch,
    findSongs
  }, dispatch)
}

export default connect (mapStateToProps, mapDispatchToProps)(SearchWidget);
