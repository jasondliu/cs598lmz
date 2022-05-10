import select from './select.jpg'

function Card(props) {
    return (
        <div className="selected-cards">
            <img src={select} alt="" />
            <img src={cur_hero} alt="" />
            <span className="card-numb">{props.count}</span>
        </div>


    )
}

function Cards(props) {
    return (
        <div className="cards">
            <img src={props.image} alt="" />
            <span className="attack-value">{props.attack}</span>
            <span className="health-value">{props.health}</span>
        </div>
    )
}
export default class Hero extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            count: 0,
            image: '',
            attack: '',
            health: '',
            card: true
        }
    }
    upClick() {
        this.setState({ count:
