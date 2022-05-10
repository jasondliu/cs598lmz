import selector from '../selector';
import { setCurrentTodo, setTodos } from '../actions';
import { IProps, IState } from '../types';
import { Selector } from 'react-redux';
import { RootState } from '../reducer';

class App extends React.Component<IProps, IState> {
  public state: IState = {
    isEditing: false,
    errorMessage: '',
  }

  public componentDidMount() {
    this.props.onLoad();
  }

  public toggleEditInput = () => {
    this.setState(prevState => ({
      isEditing: !prevState.isEditing,
    }));
  }

  public handleSetCurrentTodo = (todo: ITodo) => {
    this.props.onSetCurrentTodo(todo);
  }

  public handleCreateTodo = (title: string) => {
    const { onCreateTodo, currentTodo } = this.props;

    if (this.checkTodoExists(title
