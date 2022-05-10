import selectData from '../../selectors/datapoints';
import DataPointMap from './DataPointMap';


export class DataPointList extends React.Component {

    state={
        category: ''
    }

    componentDidMount() {
        this.props.startSetData();
    }

    render() {
        return (
            <div className="data-page">
                {/* <div className="data-page-filter">
                    <select value={this.state.category} onChange={this.onChange}>
                        <option value="">--Filter categories--</option>
                        <option value="GIS">GIS</option>
                        <option value="MODIS">MODIS</option>
                        <option value="RAWS">RAWS</option>
                        <option value="SENSORS">SENSORS</option>
                    </select>
                </div> */}
                <div className="data-page-header">
                    <DataPointSummary />
                </div>
                <div className="data-page-list">
                    {this.props
