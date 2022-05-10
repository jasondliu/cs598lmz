import selector from '../../selectors/listSelector';
import { compose } from 'redux';
import { connect } from 'react-redux';
import { withRouter } from 'react-router-dom';
import { rootState } from '../../reducers/index';
import { listActions } from '../../actions/listActions';

interface IProps {
	lists: ILists;
	setList: (id: string) => void;
	history: IHistory;
}

const Lists: React.FC<IProps> = ({ lists, setList, history }) => {
	const onSetList = (id: string) => (ev: React.MouseEvent<HTMLDivElement, MouseEvent>) => {
		ev.preventDefault();
		ev.stopPropagation();
		setList(id);
		history.push('/tasks');
	};

	return (
		<div className="lists">
			{lists &&
				Object.entries(lists).length > 0 &&
				
