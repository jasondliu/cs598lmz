import selector from './selector'

import {
    openForm,
    closeForm
} from './action'

const mapStateToProps = state => ({
    task: selector.getTask(state),
})

const mapDispatchToProps = dispatch => ({
    onOpenForm: () => dispatch(openForm()),
    onCloseForm: () => dispatch(closeForm())
})

export default connect(mapStateToProps, mapDispatchToProps)(FormContainer)
