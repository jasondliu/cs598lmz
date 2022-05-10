import selector from 'ui/utils/visualisations/selector';

class Visualisation extends Component {
  render() {
    const {
      visualisation,
      visualisation: {
        type
      },
      data
    } = this.props;

    const Component = selector(type);

    return (
      <div className="Visualisation">
        <Component
          visualisation={visualisation}
          data={data}
        />
      </div>
    );
  }
}

Visualisation.propTypes = {
  visualisation: PropTypes.object.isRequired,
  data: PropTypes.object.isRequired
};

export default Visualisation;
