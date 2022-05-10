import selectionsort from './selectionsort';
import insertionSort from './insertionsort';
import {Button} from 'react-bootstrap';

class App extends Component {
  constructor(props){
    super(props);
    this.state = {
      array: [],
    }
  }

  componentDidMount(){
    this.resetArray();
  }

  resetArray(){
    const array = [];
    for(let i = 0; i < 100; i++){
      array.push(randomIntFromInterval(5, 1000));
    }
    this.setState({array});
  }

  mergeSort(){
    const animations = getMergeSortAnimations(this.state.array);
    for(let i = 0; i < animations.length; i++){
      const arrayBars = document.getElementsByClassName('array-bar');
      const isColorChange = i % 3 !== 2;
      if(isColorChange){
        const [barOneIdx, barTwoIdx] = animations[i];
        const barOneStyle = array
