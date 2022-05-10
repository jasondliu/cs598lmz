import selectLocation from '../../selectors/locations';
import { startSetLocations } from '../../actions/locations';

export class LocationList extends React.Component{

    componentDidMount(){
        this.props.startSetLocations();
    }
    
    render(){
        return (
            <div className = "content-container">
                <div className = "list-header">
                    <div className = "show-for-mobile">Locations</div>
                    <div className = "show-for-desktop">Localizações</div>
                    <div className = "show-for-desktop">Unidades</div>
                </div>
                <div className = "list-body">
                    {
                        this.props.locations.length === 0 ? (
                            <div className = "list-item list-item--message">
                                <span>Nenhuma localização cadastrada.</span>
                            </div>
                        ) : (
                            this.props.locations.map((location)
