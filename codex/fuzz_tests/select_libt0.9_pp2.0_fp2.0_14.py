import selectedDataType from './selectedDataTypeReducer';
import dataType from './dataTypesReducer';
import selectedData from './selectedDataReducer';
import selectedApp from './selectedAppReducer';
import steps from './steps';
import step from './step';
import goToStep from './actions_goToStep';
import stepProperties from './stepsProperties';
import project from './projectsReducer';

const rootReducer = combineReducers({
	user,
	apps,
	datasets,
	selectedApp,
	selectedUser,
	dataType,
	dataTypes,
	data,
	selectedData,
	selectedDataType,
	steps,
	step,
	goToStep,
	stepProperties,
	project
})

export default rootReducer
